import stripe

from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from django.conf import settings
from service.models import Item
from service.serializers import ItemSerializer


stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response({'items': queryset}, template_name='service/item_list.html')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        context = {
            'item': instance,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY
        }
        return Response(context, template_name='service/item_detail.html')


class CreateCheckoutSessionAPI(APIView):
    def get(self, request, id, *args, **kwargs):
        item = get_object_or_404(Item, id=id)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/') + '?success=true',
            cancel_url=request.build_absolute_uri('/') + '?canceled=true',
        )
        return Response({'id': session.id})
