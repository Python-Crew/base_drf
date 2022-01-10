import json
import pytest
from django.urls import reverse
from knowledge_center.models import KnowledgeCenterCategory

categories_url = reverse("category_list")
category_detail_url = reverse("category_detail", kwargs={"pk": 1})
selected_categories_url = reverse("main_page_categories")


@pytest.mark.django_db
def test_zero_categories_should_return_empty_list(client) -> None:
    response = client.get(categories_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


@pytest.mark.django_db
def test_no_category_detail_should_fail(client) -> None:
    response = client.get(category_detail_url)
    assert response.status_code == 404
    assert json.loads(response.content) == {"detail": "Not found."}


@pytest.mark.django_db
def test_one_category_exists_should_succeed(client) -> None:
    test_category = KnowledgeCenterCategory.objects.create(title="Rock")
    response = client.get(categories_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("title") == test_category.title
    assert response_content.get("parent") == test_category.parent
    assert (
        response_content.get("main_page_category") == test_category.main_page_category
    )


@pytest.mark.django_db
def test_one_main_page_category_exists_should_succeed(client) -> None:
    test_main_page_category = KnowledgeCenterCategory.objects.create(
        title="Rock", main_page_category=True
    )
    response = client.get(selected_categories_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("title") == test_main_page_category.title
    assert response_content.get("parent") == test_main_page_category.parent
    assert (
        response_content.get("main_page_category")
        == test_main_page_category.main_page_category
    )
