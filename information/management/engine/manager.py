from django.core.paginator import Paginator

from authentication.models import CustomUser
from chat.models.discussion import Discussion
from proposition.models.proposition import Proposition
from vote.models.voting import Voting


class Manager():
    """Manager manager class.
    """
    def __init__(self):
        pass

    def set_collectivity_dashboard_context(self, request, context):
        context['custom_user_pag_obj'] = (
            self.__set_custom_user_page_obj_context(request)
        )
        context['custom_users_p_counts'] = (
            self.__set_custom_user_p_counts_context(request)
        )
        context['proposition_pag_obj'] = (
            self.__set_proposition_page_obj_context(request)
        )
        context['discussion_pag_obj'] = (
            self.__set_discussion_page_obj_context(request)
        )
        context['voting_pag_obj'] = (self.__set_voting_page_obj_context(request)
        )
        return context

    def __set_custom_user_page_obj_context(self, request):
        """This method returns Custom User page objects.
        """
        custom_users = self.__get_custom_user_queryset(request)
        paginator = Paginator(custom_users, 5)
        page_number = request.GET.get('page')
        page_objects = paginator.get_page(page_number)
        return page_objects

    def __get_custom_user_queryset(self, request):
        """This method returns a queryset of Custom User.
        """
        queryset = (
            CustomUser.objects.filter(
                collectivity_id__exact=request.user.collectivity
            ).order_by('-balance')[:25]
        )
        return queryset

    def __set_custom_user_p_counts_context(self, request):
        """This method returns a list of dictionnary items. Dictionnary keys 
        are custom user id and the counts of propositions involving that
        same custom user.
        """
        custom_user_p_counts = []
        custom_users = CustomUser.objects.filter(
            collectivity_id=request.user.collectivity
        )
        for custom_user in custom_users:
            custom_user_p_count = {'id': None, 'count':None}
            proposition_count = (
                Proposition.objects.filter(
                    proposition_creator_id=custom_user.id
                ).count()|
                Proposition.objects.filter(
                    proposition_taker_id=custom_user.id
                ).count()
            )
            custom_user_p_count['id'] = custom_user.id
            custom_user_p_count['count'] = proposition_count
            custom_user_p_counts.append(custom_user_p_count)
        return custom_user_p_counts

    def __set_proposition_page_obj_context(self, request):
        propositions = self.__get_proposition_queryset(request)
        paginator = Paginator(propositions, 5)
        page_number = request.GET.get('page')
        page_objects = paginator.get_page(page_number)
        return page_objects

    def __get_proposition_queryset(self, request):
        queryset = (
            Proposition.objects.filter(
                proposition_creator_id__collectivity_id__exact=
                request.user.collectivity
            ).order_by('-creation_date')[:25]
        )
        return queryset

    def __set_discussion_page_obj_context(self, request):
        discussions = self.__get_discussion_queryset(request)
        paginator = Paginator(discussions, 5)
        page_number = request.GET.get('page')
        page_objects = paginator.get_page(page_number)
        return page_objects

    def __get_discussion_queryset(self, request):
        queryset = (
            Discussion.objects.filter(
                discussion_custom_user_id__collectivity_id__exact=
                request.user.collectivity,
                discussion_discussion_type_id__exact=None
            ).order_by('-creation_date')[:25]
        )
        return queryset

    def __set_voting_page_obj_context(self, request):
        votings = self.__get_voting_queryset(request)
        paginator = Paginator(votings, 5)
        page_number = request.GET.get('page')
        page_objects = paginator.get_page(page_number)
        return page_objects

    def __get_voting_queryset(self, request):
        queryset = (
            Voting.objects.filter(
               voting_custom_user_id__collectivity_id__exact=
                request.user.collectivity
            ).order_by('-creation_date')[:25]
        )
        return queryset
