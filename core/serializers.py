from rest_framework import serializers
from . import models

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MenuItem
        fields = ('id', 'name', 'description', 'price', 'image', 'is_available', 'place', 'category')

class CategorySerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True, read_only=True)
    class Meta:
        model = models.Category
        fields = ('id', 'name', 'place', 'menu_items')

class PlaceDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = models.Place
        fields = ('id', 'name', 'image', 'number_of_tables', 'categories', 'font', 'color')

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Place
        fields = ('id', 'name', 'image')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"