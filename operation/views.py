
from django.shortcuts import render, redirect
from master.models import Supplier, Item
from .models import Purchase
from .forms import PurchaseForm
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

def purchase_list(request):
    return render(request , 'purchase_list.html')

def purchase_master(request):
    suppliers = Supplier.objects.filter(status=1)  # Fetch valid suppliers
    items = Item.objects.filter(status=1)  # Fetch valid items
    form = PurchaseForm()

    if request.method == 'POST':
        # Get the supplier from the POST data
        supplier_name_id = request.POST.get('supplier_name')
        if not supplier_name_id:
            return render(request, 'purchase_master.html', {'form': form, 'suppliers': suppliers, 'items': items, 'error': 'Please select a supplier.'})
        
        items_data = request.POST.getlist('items[]')  # List of item data

        if not items_data:
            return render(request, 'purchase_master.html', {'form': form, 'suppliers': suppliers, 'items': items, 'error': 'Please add at least one item.'})
        
        # Iterate over items and validate
        for item_data in items_data:
            try:
                item_name_id, quantity, total = item_data.split(',')

                # Validate item
                item_name = Item.objects.get(id=item_name_id)

                # Validate quantity and total
                if not quantity.isdigit() or not total:
                    return render(request, 'purchase_master.html', {'form': form, 'suppliers': suppliers, 'items': items, 'error': 'Invalid quantity or total.'})

                quantity = int(quantity)
                total = float(total)

                # Create Purchase entry
                Purchase.objects.create(
                    supplier_name_id=supplier_name_id,
                    item_name=item_name,
                    quantity=quantity,
                    total=total
                )
            except (ValueError, Item.DoesNotExist):
                return render(request, 'purchase_master.html', {
                    'form': form,
                    'suppliers': suppliers,
                    'items': items,
                    'error': 'There was an error processing one of the items. Please try again.'
                })

        return redirect('purchase')

    return render(request, 'purchase_master.html', {'form': form, 'suppliers': suppliers, 'items': items})



def get_item_rate(request):
    item_name_id = request.GET.get('item_name_id')  # item_name_id for AJAX
    try:
        item_name = Item.objects.get(id=item_name_id)
        return JsonResponse({'rate': item_name.unit_price})  # Returning item_name rate
    except Item.DoesNotExist:
        return JsonResponse({'rate': 0})
    
