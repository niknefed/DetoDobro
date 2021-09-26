from django.contrib import admin
from django.core.paginator import Paginator
from django.core.cache import cache
from django.db import models
from .models import PublicChatRoom, PublicRoomChatMessage


class PublicChatRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['id', 'title']
    list_display = ['id',]

    class Meta:
        model = PublicChatRoom

admin.site.register(PublicChatRoom, PublicChatRoomAdmin)

class CachingPaginator(Paginator):
    def __get__count(self):

        if not hasattr(self, "_count"):
            self.__count = None

        if self.__count is None:
            try:
                key = "adm:{0}:count".format(hash(self.object_list.query.__str__()))
                self.__count = cache.get(key,-1)
                if self.__count == -1:
                    self.__count = super().count
                    cache.set(key, self.__count, 3600)
            except:
                self.__count = len(self.object_list)
        return self.__count
    count = property(__get__count)


class PublicRoomChatMessageAdmin(admin.ModelAdmin):
    list_filter = ['room', 'user', "timestamp"]
    list_display = ['room', 'user', 'content', "timestamp"]
    search_fields = ['room__title', 'user__username', 'content']
    readonly_fields = ['id', "user", "room", "timestamp"]

    show_full_result_count = False
    paginator = CachingPaginator

    class Meta:
        model = PublicRoomChatMessage

admin.site.register(PublicRoomChatMessage, PublicRoomChatMessageAdmin)