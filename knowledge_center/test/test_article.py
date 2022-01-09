import json
import pytest
from django.urls import reverse
from knowledge_center.models import KnowledgeCenterArticle, KnowledgeCenterCategory
from user.models import User
categories_url = reverse("category_list")
articles_url = reverse("article_list")
article_rate_url = reverse("article_rate", kwargs={'pk': 1})


@pytest.mark.django_db
def test_zero_articles_should_return_empty_list(client) -> None:
    response = client.get(articles_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


@pytest.mark.django_db
def test_one_article_exists_should_succeed(client) -> None:
    author = User.objects.create(email="ghazal.hadiyan@gmail.com")
    category = KnowledgeCenterCategory.objects.filter(title="Rock")
    test_article = KnowledgeCenterArticle.objects.create(text="first article")
    test_article.author = author
    test_article.category.set(category)
    response = client.get(articles_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("text") == test_article.text



@pytest.mark.django_db
def test_create_article_rate_without_argument_should_succeed(client) -> None:
    response = client.post(path=article_rate_url)
    assert response.status_code == 200

