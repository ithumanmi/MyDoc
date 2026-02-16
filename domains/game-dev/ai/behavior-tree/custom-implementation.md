# 🛠️ Custom Behavior Tree: Tự code C# từ A-Z

> [← Back to Behavior Tree Fundamentals](./core-concepts.md)

Thay vì dùng Plugin đắt tiền, hãy tự viết một hệ thống BT đơn giản nhưng mạnh mẽ.

---

## 1. Node Base Class

Tất cả các node đều kế thừa từ class này.

```csharp
public enum NodeState { Running, Success, Failure }

public abstract class Node {
    protected NodeState state;
    public Node parent;
    protected List<Node> children = new List<Node>();

    public Node() { parent = null; }
    public Node(List<Node> children) {
        foreach (var child in children) _Attach(child);
    }

    private void _Attach(Node node) {
        node.parent = this;
        children.Add(node);
    }

    public abstract NodeState Evaluate(); // Hàm quan trọng nhất
}
```

---

## 2. Composite Nodes

### **Selector (OR)**
```csharp
public class Selector : Node {
    public Selector(List<Node> children) : base(children) {}

    public override NodeState Evaluate() {
        foreach (var node in children) {
            switch (node.Evaluate()) {
                case NodeState.Failure: continue; // Thử con tiếp theo
                case NodeState.Success: 
                    state = NodeState.Success; 
                    return state;
                case NodeState.Running: 
                    state = NodeState.Running; 
                    return state;
            }
        }
        state = NodeState.Failure; // Tất cả đều thất bại
        return state;
    }
}
```

### **Sequence (AND)**
```csharp
public class Sequence : Node {
    public Sequence(List<Node> children) : base(children) {}

    public override NodeState Evaluate() {
        bool anyChildRunning = false;
        foreach (var node in children) {
            switch (node.Evaluate()) {
                case NodeState.Failure: 
                    state = NodeState.Failure; 
                    return state;
                case NodeState.Success: continue; // Làm tiếp con sau
                case NodeState.Running: 
                    anyChildRunning = true; 
                    continue;
            }
        }
        state = anyChildRunning ? NodeState.Running : NodeState.Success;
        return state;
    }
}
```

---

## 3. Leaf Nodes (Action Example)

```csharp
public class TaskGoToTarget : Node {
    private Transform _transform;
    private Transform _target;

    public TaskGoToTarget(Transform transform, Transform target) {
        _transform = transform;
        _target = target;
    }

    public override NodeState Evaluate() {
        if (Vector3.Distance(_transform.position, _target.position) < 0.1f) {
            state = NodeState.Success;
            return state;
        }
        
        // Logic di chuyển
        _transform.position = Vector3.MoveTowards(
            _transform.position, _target.position, Time.deltaTime);
            
        state = NodeState.Running;
        return state;
    }
}
```

---

## 4. Tree Runner (MonoBehaviour)

Script gắn vào GameObject để chạy cây.

```csharp
public class BossAI : MonoBehaviour {
    private Node _rootNode;

    void Start() {
        _rootNode = SetupTree();
    }

    void Update() {
        if (_rootNode != null) _rootNode.Evaluate();
    }

    private Node SetupTree() {
        // Xây dựng cây bằng code
        Node root = new Selector(new List<Node> {
            new Sequence(new List<Node> {
                new CheckEnemyInrange(transform),
                new TaskAttack(transform)
            }),
            new TaskPatrol(transform, waypoints)
        });
        return root;
    }
}
```
