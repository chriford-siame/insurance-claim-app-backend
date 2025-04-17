from rest_framework.routers import DefaultRouter

from claim.viewsets import (
    UserViewSet    ,
    ClaimantViewSet,
    ReviewerViewSet
)

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'claimants', ClaimantViewSet, basename='claimant')
router.register(r'reviewers', ReviewerViewSet, basename='reviewer')

app_name = 'claim'
urlpatterns = router.urls
