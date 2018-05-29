
from surveymonty import utils
from surveymonty.client import BaseClient

class ClientV3(BaseClient):
    version = 'v3'

    def get_me(self, **request_kwargs):
        endpoint = '/users/me'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_groups(self, **request_kwargs):
        endpoint = '/groups'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_group(self, group_id, **request_kwargs):
        endpoint = '/groups/{group_id}'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_group_members(self, group_id, **request_kwargs):
        endpoint = '/groups/{group_id}/members'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_group_member(self, group_id, member_id, **request_kwargs):
        endpoint = '/groups/{group_id}/members/{member_id}'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_surveys(self, **request_kwargs):
        endpoint = '/surveys'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def create_survey(self, **request_kwargs):
        endpoint = '/surveys'.format(**locals())

        return self._request('POST', endpoint, self.access_token, **request_kwargs)

    def get_survey(self, survey_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def update_survey(self, survey_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}'.format(**locals())

        return self._request('PATCH', endpoint, self.access_token, **request_kwargs)

    def upsert_survey(self, survey_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}'.format(**locals())

        return self._request('PUT', endpoint, self.access_token, **request_kwargs)

    def delete_survey(self, survey_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}'.format(**locals())

        return self._request('DELETE', endpoint, self.access_token, **request_kwargs)

    def get_survey_details(self, survey_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/details'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_survey_categories(self, **request_kwargs):
        endpoint = '/survey_categories'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_survey_templates(self, **request_kwargs):
        endpoint = '/survey_templates'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_survey_pages(self, survey_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def create_survey_page(self, survey_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages'.format(**locals())

        return self._request('POST', endpoint, self.access_token, **request_kwargs)

    def get_survey_page(self, survey_id, page_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages/{page_id}'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def update_survey_page(self, survey_id, page_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages/{page_id}'.format(**locals())

        return self._request('PATCH', endpoint, self.access_token, **request_kwargs)

    def upsert_survey_page(self, survey_id, page_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages/{page_id}'.format(**locals())

        return self._request('PUT', endpoint, self.access_token, **request_kwargs)

    def delete_survey_page(self, survey_id, page_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages/{page_id}'.format(**locals())

        return self._request('DELETE', endpoint, self.access_token, **request_kwargs)

    def get_survey_page_questions(self, survey_id, page_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages/{page_id}/questions'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def create_survey_page_question(self, survey_id, page_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages/{page_id}/questions'.format(**locals())

        return self._request('POST', endpoint, self.access_token, **request_kwargs)

    def get_survey_page_question(self, survey_id, page_id, question_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages/{page_id}/questions/{question_id}'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def update_survey_page_question(self, survey_id, page_id, question_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages/{page_id}/questions/{question_id}'.format(**locals())

        return self._request('PATCH', endpoint, self.access_token, **request_kwargs)

    def upsert_survey_page_question(self, survey_id, page_id, question_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages/{page_id}/questions/{question_id}'.format(**locals())

        return self._request('PUT', endpoint, self.access_token, **request_kwargs)

    def delete_survey_page_question(self, survey_id, page_id, question_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages/{page_id}/questions/{question_id}'.format(**locals())

        return self._request('DELETE', endpoint, self.access_token, **request_kwargs)

    def get_contact_lists(self, **request_kwargs):
        endpoint = '/contact_lists'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def create_contact_list(self, **request_kwargs):
        endpoint = '/contact_lists'.format(**locals())

        return self._request('POST', endpoint, self.access_token, **request_kwargs)

    def get_contact_list(self, list_id, **request_kwargs):
        endpoint = '/contact_lists/{list_id}'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def update_contact_list(self, list_id, **request_kwargs):
        endpoint = '/contact_lists/{list_id}'.format(**locals())

        return self._request('PATCH', endpoint, self.access_token, **request_kwargs)

    def upsert_contact_list(self, list_id, **request_kwargs):
        endpoint = '/contact_lists/{list_id}'.format(**locals())

        return self._request('PUT', endpoint, self.access_token, **request_kwargs)

    def delete_contact_list(self, list_id, **request_kwargs):
        endpoint = '/contact_lists/{list_id}'.format(**locals())

        return self._request('DELETE', endpoint, self.access_token, **request_kwargs)

    def copy_contact_list(self, list_id, **request_kwargs):
        endpoint = '/contact_lists/{list_id}/copy'.format(**locals())

        return self._request('POST', endpoint, self.access_token, **request_kwargs)

    def merge_contact_list(self, list_id, **request_kwargs):
        endpoint = '/contact_lists/{list_id}/merge'.format(**locals())

        return self._request('POST', endpoint, self.access_token, **request_kwargs)

    def get_contact_list_contacts(self, list_id, **request_kwargs):
        endpoint = '/contact_lists/{list_id}/contacts'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def create_contact_list_contact(self, list_id, **request_kwargs):
        endpoint = '/contact_lists/{list_id}/contacts'.format(**locals())

        return self._request('POST', endpoint, self.access_token, **request_kwargs)

    def bulk_get_contact_list_contacts(self, list_id, **request_kwargs):
        endpoint = '/contact_lists/{list_id}/contacts/bulk'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def bulk_create_contact_list_contacts(self, list_id, **request_kwargs):
        endpoint = '/contact_lists/{list_id}/contacts/bulk'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_contacts(self, **request_kwargs):
        endpoint = '/contacts'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def bulk_get_contacts(self, **request_kwargs):
        endpoint = '/contacts/bulk'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def bulk_create_contacts(self, **request_kwargs):
        endpoint = '/contacts/bulk'.format(**locals())

        return self._request('POST', endpoint, self.access_token, **request_kwargs)

    def get_contact(self, contact_id, **request_kwargs):
        endpoint = '/contacts/{contact_id}'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def update_contact(self, contact_id, **request_kwargs):
        endpoint = '/contacts/{contact_id}'.format(**locals())

        return self._request('PATCH', endpoint, self.access_token, **request_kwargs)

    def upsert_contact(self, contact_id, **request_kwargs):
        endpoint = '/contacts/{contact_id}'.format(**locals())

        return self._request('PUT', endpoint, self.access_token, **request_kwargs)

    def delete_contact(self, contact_id, **request_kwargs):
        endpoint = '/contacts/{contact_id}'.format(**locals())

        return self._request('DELETE', endpoint, self.access_token, **request_kwargs)

    def get_contact_fields(self, **request_kwargs):
        endpoint = '/contact_fields'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_contact_field(self, field_id, **request_kwargs):
        endpoint = '/contact_fields/{field_id}'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def update_contact_field(self, field_id, **request_kwargs):
        endpoint = '/contact_fields/{field_id}'.format(**locals())

        return self._request('PATCH', endpoint, self.access_token, **request_kwargs)

    def get_survey_collectors(self, survey_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/collectors'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def create_survey_collector(self, survey_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/collectors'.format(**locals())

        return self._request('POST', endpoint, self.access_token, **request_kwargs)

    def get_collector(self, collector_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def update_collector(self, collector_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}'.format(**locals())

        return self._request('PATCH', endpoint, self.access_token, **request_kwargs)

    def upsert_collector(self, collector_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}'.format(**locals())

        return self._request('PUT', endpoint, self.access_token, **request_kwargs)

    def delete_collector(self, collector_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}'.format(**locals())

        return self._request('DELETE', endpoint, self.access_token, **request_kwargs)

    def get_collector_messages(self, collector_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/messages'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def create_collector_message(self, collector_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/messages'.format(**locals())

        return self._request('POST', endpoint, self.access_token, **request_kwargs)

    def get_collector_message(self, collector_id, message_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/messages/{message_id}'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def update_collector_message(self, collector_id, message_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/messages/{message_id}'.format(**locals())

        return self._request('PATCH', endpoint, self.access_token, **request_kwargs)

    def upsert_collector_message(self, collector_id, message_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/messages/{message_id}'.format(**locals())

        return self._request('PUT', endpoint, self.access_token, **request_kwargs)

    def delete_collector_message(self, collector_id, message_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/messages/{message_id}'.format(**locals())

        return self._request('DELETE', endpoint, self.access_token, **request_kwargs)

    def send_collector_message(self, collector_id, message_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/messages/{message_id}/send'.format(**locals())

        return self._request('POST', endpoint, self.access_token, **request_kwargs)

    def get_collector_message_recipients(self, collector_id, message_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/messages/{message_id}/recipients'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def create_collector_message_recipient(self, collector_id, message_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/messages/{message_id}/recipients'.format(**locals())

        return self._request('POST', endpoint, self.access_token, **request_kwargs)

    def bulk_create_collector_message_recipients(self, collector_id, message_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/messages/{message_id}/recipients/bulk'.format(**locals())

        return self._request('POST', endpoint, self.access_token, **request_kwargs)

    def get_collector_recipients(self, collector_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/recipients'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_collector_recipient(self, collector_id, recipient_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/recipients/{recipient_id}'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def delete_collector_recipient(self, collector_id, recipient_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/recipients/{recipient_id}'.format(**locals())

        return self._request('DELETE', endpoint, self.access_token, **request_kwargs)

    def get_survey_responses(self, survey_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/responses'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_collector_responses(self, collector_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/responses'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def create_collector_response(self, collector_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/responses'.format(**locals())

        return self._request('POST', endpoint, self.access_token, **request_kwargs)

    def bulk_get_survey_responses(self, survey_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/responses/bulk'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def bulk_get_collector_responses(self, collector_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/responses/bulk'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_survey_response(self, survey_id, responses_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/responses/{responses_id}'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def update_survey_response(self, survey_id, responses_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/responses/{responses_id}'.format(**locals())

        return self._request('PATCH', endpoint, self.access_token, **request_kwargs)

    def upsert_survey_response(self, survey_id, responses_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/responses/{responses_id}'.format(**locals())

        return self._request('PUT', endpoint, self.access_token, **request_kwargs)

    def delete_survey_response(self, survey_id, responses_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/responses/{responses_id}'.format(**locals())

        return self._request('DELETE', endpoint, self.access_token, **request_kwargs)

    def get_collector_response(self, collector_id, responses_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/responses/{responses_id}'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def update_collector_response(self, collector_id, responses_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/responses/{responses_id}'.format(**locals())

        return self._request('PATCH', endpoint, self.access_token, **request_kwargs)

    def upsert_collector_response(self, collector_id, responses_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/responses/{responses_id}'.format(**locals())

        return self._request('PUT', endpoint, self.access_token, **request_kwargs)

    def delete_collector_response(self, collector_id, responses_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/responses/{responses_id}'.format(**locals())

        return self._request('DELETE', endpoint, self.access_token, **request_kwargs)

    def get_survey_response_details(self, survey_id, responses_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/responses/{responses_id}/details'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_collector_response_details(self, collector_id, responses_id, **request_kwargs):
        endpoint = '/collectors/{collector_id}/responses/{responses_id}/details'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_survey_rollups(self, survey_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/rollups'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_survey_page_rollups(self, survey_id, page_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages/{page_id}/rollups'.format(**locals())

        return self._request('get', endpoint, self.access_token, **request_kwargs)

    def get_survey_page_question_rollups(self, survey_id, page_id, question_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages/{page_id}/questions/{question_id}/rollups'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_survey_trends(self, survey_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/trends'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_survey_page_trends(self, survey_id, page_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages/{page_id}/trends'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_survey_page_question_trends(self, survey_id, page_id, question_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages/{page_id}/questions/{question_id}/trends'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_webhooks(self, **request_kwargs):
        endpoint = '/webhooks'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def create_webhook(self, **request_kwargs):
        endpoint = '/webhooks'.format(**locals())

        return self._request('POST', endpoint, self.access_token, **request_kwargs)

    def get_webhook(self, webhook_id, **request_kwargs):
        endpoint = '/webhooks/{webhook_id}'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def update_webhook(self, webhook_id, **request_kwargs):
        endpoint = '/webhooks/{webhook_id}'.format(**locals())

        return self._request('PATCH', endpoint, self.access_token, **request_kwargs)

    def upsert_webhook(self, webhook_id, **request_kwargs):
        endpoint = '/webhooks/{webhook_id}'.format(**locals())

        return self._request('PUT', endpoint, self.access_token, **request_kwargs)

    def delete_webhook(self, webhook_id, **request_kwargs):
        endpoint = '/webhooks/{webhook_id}'.format(**locals())

        return self._request('DELETE', endpoint, self.access_token, **request_kwargs)

    def get_benchmark_bundles(self, **request_kwargs):
        endpoint = '/benchmark_bundles'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_benchmark_bundle(self, bundle_id, **request_kwargs):
        endpoint = '/benchmark_bundles/{bundle_id}'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_benchmark_bundle_analysis(self, bundle_id, **request_kwargs):
        endpoint = '/benchmark_bundles/{bundle_id}/analyze'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_survey_page_question_benchmark(self, survey_id, page_id, question_id, **request_kwargs):
        endpoint = '/surveys/{survey_id}/pages/{page_id}/questions/{question_id}/benchmark'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_errors(self, **request_kwargs):
        endpoint = '/errors'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)

    def get_error(self, error_id, **request_kwargs):
        endpoint = '/errors/{error_id}'.format(**locals())

        return self._request('GET', endpoint, self.access_token, **request_kwargs)
