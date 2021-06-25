from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSets, generete_pdf

router = DefaultRouter()
router.register("invoices", InvoiceViewSets, basename="invoices")

urlpatterns = [
    path('', include(router.urls)),
    path('invoices/<int:invoice_id>/generete_pdf/', generete_pdf, name='generete_pdf'),
]