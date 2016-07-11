from recipe_site.models.user_profile import UserProfile
from recipe_site.serializers.user_profile import UserProfileSerializer


def user_profile_context(request):

    user_profiles = UserProfile.objects.filter(user=request.user)
    current_user_profile = UserProfileSerializer(user_profiles,
                                                context={'request': request}, many=True).data

    return {'users': current_user_profile}
