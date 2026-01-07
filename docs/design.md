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

| 画面名 | パス (例) | 機能概要 |
| :--- | :--- | :--- |
| **一覧画面** | `/` | Todoの一覧表示、新規作成（クイック追加）、完了切り替え、削除 |
| **詳細画面** | `/todos/:id` | Todoの全ての情報（詳細、期間など）を表示 |
| **編集画面** | `/todos/:id/edit` | タイトル、詳細、開始・終了日時の編集 |
