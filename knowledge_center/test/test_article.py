import json
import pytest
from django.urls import reverse
from knowledge_center.models import (
    ArticleRate,
    KnowledgeCenterArticle,
    KnowledgeCenterCategory,
)
from user.models import User

articles_url = reverse("article_list")
article_detail_url = reverse("article_detail", kwargs={"pk": 1})
article_rate_url = reverse("article_rate", kwargs={"pk": 1})


@pytest.mark.django_db
def test_zero_articles_should_return_empty_list(client) -> None:
    response = client.get(articles_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


@pytest.mark.django_db
def test_no_article_detail_should_fail(client) -> None:
    response = client.get(article_detail_url)
    assert response.status_code == 404
    assert json.loads(response.content) == {"detail": "Not found."}


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
def test_no_article_rate_should_fail(client) -> None:
    response = client.get(article_rate_url)
    assert response.status_code == 404
    assert json.loads(response.content) == {"detail": "Not found."}


@pytest.mark.django_db
def test_one_article_rate_exists_should_succeed(client) -> None:
    test_author = User.objects.create(email="ghazal.hadiyan@gmail.com")
    test_category = KnowledgeCenterCategory.objects.filter(title="Rock")
    test_article = KnowledgeCenterArticle.objects.create(text="first article")
    test_article.author = test_author
    test_article.category.set(test_category)
    test_rate = ArticleRate.objects.create(article=test_article, rate=4.0)
    response = client.get(article_rate_url)
    response_content = json.loads(response.content)
    assert response.status_code == 200
    assert response_content.get("rate") == test_rate.rate


@pytest.mark.django_db
def test_create_article_rate_without_argument_should_fail(client) -> None:
    response = client.post(path=article_rate_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "article": ["This field is required."],
        "rate": ["This field is required."],
    }


@pytest.mark.django_db
def test_create_multi_article_rate_should_succeed(client) -> None:
    test_author = User.objects.create(email="ghazal.hadiyan@gmail.com")
    test_category = KnowledgeCenterCategory.objects.filter(title="Rock")
    test_article = KnowledgeCenterArticle.objects.create(text="first article")
    test_article.author = test_author
    test_article.category.set(test_category)
    test_rate1 = ArticleRate.objects.create(article=test_article, rate=4.0)
    test_rate2 = ArticleRate.objects.create(article=test_article, rate=4.5)
    test_rate3 = ArticleRate.objects.create(article=test_article, rate=3.5)
    response = client.get(article_detail_url)
    assert response.status_code == 200
    assert json.loads(response.content)["avg_rate"] == test_article.avg_rate
