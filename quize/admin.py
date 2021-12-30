from django.contrib import admin
from . import models


@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
    ]


class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = ["answer_text", "is_right"]


@admin.register(models.Questions)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "quizzes",
    ]
    list_display = ["title", "quizzes", "date_updated"]
    inlines = [
        AnswerInlineModel,
    ]


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["answer_text", "is_right", "question"]


# from django.contrib import admin
# from quize.models import Category,Quizzes,Questions,Answer


# class CategoryAdmin(admin.ModelAdmin):
#     """category model fields list display"""

#     list_display = (
#         "id",
#         "name"
#     )

# class QuizzesAdmin(admin.ModelAdmin):
#     """category model fields list display"""

#     list_display = (
#         "id",
#         "category",
#         "title",
#         "date_created"
#     )

# class QuestionsAdmin(admin.ModelAdmin):
#     """category model fields list display"""

#     list_display = (
#         "id",
#         "quizzes",
#         "technique",
#         "title",
#         "difficulty",
#         "date_created",
#         "is_active",
#     )

# class AnswerAdmin(admin.ModelAdmin):
#     """category model fields list display"""

#     list_display = (
#         "id",
#         "question",
#         "answer_text",
#         "is_right"

#     )


# admin.site.register(Category,CategoryAdmin)
# admin.site.register(Quizzes,QuizzesAdmin)
# admin.site.register(Questions,QuestionsAdmin)
# admin.site.register(Answer,AnswerAdmin)
