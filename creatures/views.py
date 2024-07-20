import json
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from .models import Creature
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def creature_list(request):
    if request.method == "GET":
        creatures = Creature.objects.all()
        creatures_list = list(creatures.values())
        return JsonResponse(creatures_list, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        creature = Creature.objects.create(**data)
        return JsonResponse({"id": creature.id}, status=201)
    else:
        return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def creature_detail(request, id):
    creature = get_object_or_404(Creature, id=id)
    if request.method == "GET":
        return JsonResponse(
            {
                "id": creature.id,
                "name": creature.name,
                "description": creature.description,
                "ability": creature.ability,
                "power": creature.power,
                "defense": creature.defense,
            }
        )
    elif request.method == "PUT":
        data = json.loads(request.body)
        for key, value in data.items():
            setattr(creature, key, value)
        creature.save()
        return JsonResponse({"id": creature.id})
    elif request.method == "DELETE":
        creature.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])
