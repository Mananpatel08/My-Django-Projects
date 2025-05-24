from django.contrib import admin
from .models import Member, Track, Wallet
from django.http import HttpResponse

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name' , )

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('date' , 'weekday' , 'total_price' , 'total_tiffins' , 'per_person_price' , 'eat_by_details')
    actions = ["export_to_txt"]
    
    def export_to_txt(self, request, queryset):
        response = HttpResponse(content_type="text/plain")
        response["Content-Disposition"] = 'attachment; filename="tiffin_data.txt"'

        # Table Header
        header = "{:<15} | {:<10} | {:<20}\n".format(
            "Member Name", "Tiffins Eaten", "Total Amount Owed"
        )
        response.write(header)
        response.write("=" * 50 + "\n")  # Separator line

        # Count how many times each member has eaten
        member_tiffin_count = {}
        total_amount_per_member = {}

        for track in queryset:
            for member in track.eat_by.all():
                if member in member_tiffin_count:
                    member_tiffin_count[member] += 1
                else:
                    member_tiffin_count[member] = 1

        # Fetch wallet details
        for member, count in member_tiffin_count.items():
            wallet = Wallet.objects.filter(member=member).first()
            total_amount_owed = wallet.total_amount if wallet else 0
            row = "{:<15} | {:<10} | {:<20}\n".format(
                member.name, count, total_amount_owed
            )
            response.write(row)

        return response

    export_to_txt.short_description = "Export tiffin summary to TXT"

@admin.register(Wallet)
class WallerAdmin(admin.ModelAdmin):
    list_display = ('member' , 'total_amount')