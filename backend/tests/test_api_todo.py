def test_read_todo(client, sample_todo):
    # Act:正常系テスト
    response = client.get(f"/api/todos/{sample_todo.id}")
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["title"] == "test"

    # Act:異常系テスト
    not_found_id = sample_todo.id + 1
    error_response = client.get(f"/api/todos/{not_found_id}")
    assert error_response.status_code == 404


def test_post_todo_success(client):
    good_request = {"title": "test", "description": "this is test"}
    response = client.post(f"/api/todos/", json=good_request)
    response_json = response.json()
    assert response.status_code == 201
    assert response_json["title"] == "test"


def test_post_todo_fail(client):
    bad_request = {"title": "", "discrption": "this is test"}
    # Act
    response = client.post(f"/api/todos/", json=bad_request)
    assert response.status_code == 422


def test_patch_todo_success(client, sample_todo):
    good_request = {"title": "updated", "description": "this isupdated"}
    response = client.patch(f"/api/todos/{sample_todo.id}", json=good_request)
    assert response.status_code == 200


def test_patch_todo_fail(client, sample_todo):
    good_request = {"title": "updated", "description": "this isupdated"}
    not_found_error_response = client.patch(
        f"/api/todos/{sample_todo.id + 1}", json=good_request
    )
    assert not_found_error_response.status_code == 404


def test_delete_todo(client, sample_todo):
    # 正常系
    response = client.delete(f"/api/todos/{sample_todo.id}")
    assert response.status_code == 204
    # 異常系
    bad_response = client.delete(f"/api/todos/{sample_todo.id + 1}")
    assert bad_response.status_code == 404
