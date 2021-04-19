from django.contrib.auth import get_user_model


def block_user(pk):
    user = get_user_model().objects.get(pk=pk)
    user.is_active = False
    user.save()


def unblock_user(pk):
    user = get_user_model().objects.get(pk=pk)
    user.is_active = True
    user.save()


def delete_user(pk):
    user = get_user_model().objects.get(pk=pk)
    user.delete()