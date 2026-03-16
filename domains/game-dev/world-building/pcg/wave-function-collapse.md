---
title: "Wave Function Collapse"
description: "WFC implementation, constraint solving, tiling rules."
tags:
  - pcg
  - wfc
  - unity
updated: 2026-03-11
---

# 🧠 Wave Function Collapse (WFC)

## 1) Concepts
- Grid of cells, mỗi cell có tập tile khả dụng (superposition).
- Chọn cell entropy thấp nhất → collapse thành tile cụ thể → propagate constraints.
- Constraint = adjacency rule (tile A có thể đứng cạnh B ở hướng N/E/S/W).
- Deterministic vs stochastic: random weight khi chọn tile.

## 2) Pipeline
1. **Sample tileset**: sprite/tile + metadata (sockets edges).
2. **Extract rules**: define allowed neighbors per direction.
3. **Initialize grid**: mỗi cell có tập tile full.
4. **Collapse loop**:
   - Pick cell entropy thấp nhất (ít lựa chọn nhất).
   - Random tile theo weight; assign.
   - Propagate: update neighbor cell, remove tile không hợp lệ.
   - Nếu cell rỗng → cần backtrack hoặc restart.
5. **Post-process**: spawn prefab, connect navmesh, add decoration.

## 3) Constraints & Backtracking
- Soft vs hard constraints: soft = prefer; hard = block.
- Backtracking: lưu stack state, khi contradiction thì revert cell, thử tile khác.
- Heuristic: tie-break random, bias theo theme (forest vs desert).
- Boundary rules: set fixed tile (edge, entry) trước khi run WFC.

## 4) Optimizations
- Use bitmask/bitset cho tile options (fast intersection).
- Jobs/Burst: propagate constraints song song theo wavefront.
- Chunk-based WFC: generate 16x16 chunk, stitch seam rule.
- Precompute canonical patterns (3x3) để accelerate rule lookup.

## 5) Unity Implementation Tips
- ScriptableObject tile definition: sprite, prefab, sockets, rotation variants.
- Use priority queue (entropy) cho chọn cell; fallback random cell khi tie-broken.
- Debug view: color code entropy, highlight contradictions.
- Save seed và collapsed grid cho replay/patch.

### Sample C# (Entropy Queue + Propagation)

```csharp
public class WFCSolver
{
    public struct Cell
    {
        public BitArray Options; // mỗi bit = tile khả dụng
        public bool IsCollapsed => Options.Count == 1;
    }

    readonly PriorityQueue<int, int> _queue = new();
    readonly List<int>[] _neighbors; // adjacency list index
    readonly Cell[] _cells;

    public WFCSolver(int cellCount, List<int>[] neighbors, int tileCount)
    {
        _cells = new Cell[cellCount];
        _neighbors = neighbors;
        for (int i = 0; i < cellCount; i++)
            _cells[i].Options = new BitArray(tileCount, true);
        EnqueueAll();
    }

    void EnqueueAll()
    {
        for (int i = 0; i < _cells.Length; i++)
        {
            int entropy = _cells[i].Options.Cardinality();
            _queue.Enqueue(i, entropy);
        }
    }

    public bool Step(int[,] allowed)
    {
        if (_queue.Count == 0) return false;
        _queue.TryDequeue(out int cellIndex, out _);
        Collapse(cellIndex);
        Propagate(cellIndex, allowed);
        return true;
    }

    void Collapse(int cellIndex)
    {
        BitArray options = _cells[cellIndex].Options;
        int choice = options.RandomSetBit();
        options.SetAll(false);
        options.Set(choice, true);
    }

    void Propagate(int source, int[,] allowed)
    {
        Queue<int> wave = new();
        wave.Enqueue(source);
        while (wave.Count > 0)
        {
            int current = wave.Dequeue();
            foreach (int neighbor in _neighbors[current])
            {
                bool changed = Restrict(neighbor, current, allowed);
                if (changed)
                    wave.Enqueue(neighbor);
            }
        }
    }

    bool Restrict(int target, int source, int[,] allowed)
    {
        // allowed[sourceTile, direction] bitmask tile
        BitArray before = (BitArray)_cells[target].Options.Clone();
        _cells[target].Options.And(ComputeMaskFromSource(source, allowed));
        return !before.XnorEquals(_cells[target].Options);
    }
}
```

- `BitArray.Cardinality()` và `RandomSetBit()` là extension helpers để đếm/ chọn tile.
- PriorityQueue dựa entropy (số option). Sau khi collapse, propagate constraints theo wave.
- `allowed` matrix lưu adjacency rules (tile × direction).
- Cần thêm logic backtracking/restart khi `Options` rỗng.

### Backtracking Extension Example

```csharp
public class BacktrackingWFCSolver : WFCSolver
{
    readonly Stack<StateSnapshot> _stack = new();
    readonly System.Random _rng;
    int _maxRetries = 64;

    struct StateSnapshot
    {
        public Cell[] Cells;
        public PriorityQueue<int, int> Queue;
    }

    public BacktrackingWFCSolver(int cells, List<int>[] neighbors, int tileCount, int seed)
        : base(cells, neighbors, tileCount)
    {
        _rng = new System.Random(seed);
    }

    public bool Solve(int[,] allowed)
    {
        int retries = 0;
        while (!IsComplete() && retries < _maxRetries)
        {
            PushState();
            bool success = Step(allowed);
            if (!success || HasContradiction())
            {
                retries++;
                bool rolledBack = PopStateAndRetry();
                if (!rolledBack) return false; // no states left
            }
        }
        return IsComplete();
    }

    void PushState()
    {
        _stack.Push(new StateSnapshot
        {
            Cells = CloneCells(),
            Queue = CloneQueue()
        });
    }

    bool PopStateAndRetry()
    {
        if (_stack.Count == 0) return false;
        var snapshot = _stack.Pop();
        Restore(snapshot);
        // random tweak: disable recently chosen tile to avoid same contradiction
        ForceDifferentChoice();
        return true;
    }

    void ForceDifferentChoice()
    {
        int cell = PickRandomCollapsedCell();
        if (cell < 0) return;
        int chosen = GetCollapsedTile(cell);
        // reopen options except chosen
        var options = GetCell(cell).Options;
        options.SetAll(true);
        options.Set(chosen, false);
        Reenqueue(cell);
    }
}
```

- `PushState` snapshot cell option + priority queue; có thể tối ưu bằng copy-on-write/struct.
- `Solve` loop gọi `Step`. Nếu contradiction (`Options` rỗng) → Pop state và thử option khác.
- `ForceDifferentChoice` mở lại cell đã collapse và loại tile vừa fail để tránh lặp vô hạn.
- `_maxRetries` giới hạn backtracking depth; log seed + retries để debug.

## ✅ Apply it
- [ ] Chuẩn hóa tile rules (socket per direction), define rotation variants.
- [ ] Implement entropy-based selection + propagation; handle contradiction.
- [ ] Backtracking/restart logic khi grid deadlock.
- [ ] Chunk WFC + seam constraints để scale map lớn.
- [ ] Debug UI cho entropy, tile options; expose seed cho designer.