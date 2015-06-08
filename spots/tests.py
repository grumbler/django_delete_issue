from django.test import TestCase

from spots.models import Spot, Derivative, SimpleDerivative


class CreateAndDeleteTest(TestCase):
    def test_delete_pk_derivative_entries(self):
        spot1 = Spot.objects.create(name='name 1')
        spot2 = Spot.objects.create(name='name 2')

        Derivative.objects.create(spot=spot1)
        Derivative.objects.create(spot=spot2)

        Derivative.objects.filter(spot__name__icontains='name').delete()

    def test_delete_simple_derivative_entries(self):
        spot1 = Spot.objects.create(name='name 1')
        spot2 = Spot.objects.create(name='name 2')

        SimpleDerivative.objects.create(spot=spot1)
        SimpleDerivative.objects.create(spot=spot2)

        SimpleDerivative.objects.filter(spot__name__icontains='name').delete()
