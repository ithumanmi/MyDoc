# 🎨 Visual Editor with GraphView: Kéo thả AI

> [← Back to Behavior Tree Fundamentals](./core-concepts.md)

Code cây bằng tay (hard-code) rất khổ sở khi cây lớn. Hãy xây dựng một Editor Window để kéo thả Node như Unreal Blueprint.

---

## 1. Setup GraphView

Unity cung cấp API `UnityEditor.Experimental.GraphView` (dùng để làm Shader Graph).

### **Các thành phần chính:**
1.  **BehaviorTreeEditor (EditorWindow):** Cửa sổ chính.
2.  **BehaviorTreeView (GraphView):** Vùng làm việc (Canvas) để vẽ node.
3.  **NodeView (Node):** Giao diện của từng node (có Input/Output port).
4.  **InspectorView:** Để chỉnh sửa thuộc tính của Node được chọn (ví dụ: tốc độ chạy, mục tiêu).

---

## 2. Lưu trữ dữ liệu (Persistence)

GraphView chỉ là giao diện (UI). Bạn cần lưu cấu trúc cây vào file (Disk).

### **ScriptableObject là chân ái:**
*   `BehaviorTree` (ScriptableObject): Chứa danh sách `nodes`.
*   Mỗi `Node` cũng là một `ScriptableObject` con (dùng `AssetDatabase.AddObjectToAsset` để nhét hết vào 1 file).

```csharp
[CreateAssetMenu()]
public class BehaviorTree : ScriptableObject {
    public Node rootNode;
    public NodeState treeState = NodeState.Running;
    public List<Node> nodes = new List<Node>();

    public NodeState Update() {
        if (rootNode.state == NodeState.Running) 
            treeState = rootNode.Evaluate();
        return treeState;
    }
}
```

---

## 3. Quy trình tạo Editor (Các bước)

1.  **Tạo file UXML (UI Builder):** Thiết kế layout (Cửa sổ trái là Tree View, Phải là Inspector).
2.  **Override `PopulateView()`:** Load file UXML và add vào cửa sổ Editor.
3.  **Implement `GraphView.GetCompatiblePorts()`:** Quy định Node nào nối được với Node nào (Output của Selector chỉ nối được vào Input của Task).
4.  **OnGraphViewChanged:** Khi người dùng nối dây hoặc xóa node trên UI -> Cập nhật danh sách `children` trong ScriptableObject.

---

## 4. Debugging (Gỡ lỗi trực quan)

Làm sao biết cây đang chạy đến đâu?

*   Trong hàm `Update()` của Editor, kiểm tra `node.state`.
*   Nếu `Running`: Tô viền Node màu vàng.
*   Nếu `Success`: Tô màu xanh.
*   Nếu `Failure`: Tô màu đỏ.
*   -> Bạn sẽ thấy luồng AI chạy thời gian thực (Runtime Visualization).
