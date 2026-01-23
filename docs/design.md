# 設計書

## 1. ER図

```mermaid
erDiagram
    todos {
        bigint id PK "一意のID"
        varchar title "タスク名"
        text description "詳細"
        timestamp start_date "開始日時"
        timestamp end_date "終了日時"
        boolean completed "完了したか (status)"
        timestamp created_at "作成日時"
        timestamp updated_at "更新日時"
    }
```

## 2. 画面遷移図

```mermaid
flowchart TD
    %% ノード（画面）の定義
    List["<b>一覧画面</b><br/>(Todo List)"]
    Detail["<b>詳細画面</b><br/>(View Detail)"]
    Edit["<b>編集画面</b><br/>(Edit Form)"]

    %% メインの遷移
    List ---->|クリック| Detail
    List ---->|編集ボタン| Edit
    Detail -->|編集ボタン| Edit

    %% 戻る・保存の遷移
    Edit -->|保存・キャンセル| Detail
    Detail -->|戻る| List

    %% 画面内アクション（右側にまとめる）
    List -.-> Action1["追加 (Enter)"]
    List -.-> Action2["完了/未完了"]
    List -.-> Action3["削除"]

    %% スタイルの設定（見栄えを良くする）
    style List fill:#f9f,stroke:#333,stroke-width:2px
    style Detail fill:#bbf,stroke:#333,stroke-width:2px
    style Edit fill:#bfb,stroke:#333,stroke-width:2px
```
### 画面詳細
| メソッド | エンドポイント | 機能 |
|----------|---------------|------|
| `GET` | `/api/todos` | Todo一覧取得 |
| `GET` | `/api/todos/:id` | 特定のTodo取得 |
| `POST` | `/api/todos` | 新規Todo作成 |
| `PUT` | `/api/todos/:id` | Todo更新 |
| `DELETE` | `/api/todos/:id` | Todo削除 |
