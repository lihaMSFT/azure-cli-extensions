# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


class Update(AAZCommand):
    """Update a new customer communication to an Azure support ticket.
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.support/supporttickets/{}/communications/{}", "2024-04-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.communication_name = AAZStrArg(
            options=["-n", "--name", "--communication-name"],
            help="Communication name.",
            required=True,
        )
        _args_schema.ticket_name = AAZStrArg(
            options=["--ticket-name"],
            help="Support ticket name.",
            required=True,
        )
        _args_schema.communication_body = AAZStrArg(
            options=["--communication-body"],
            help="Body of the communication.",
        )
        _args_schema.communication_sender = AAZStrArg(
            options=["--communication-sender"],
            help="Email address of the sender. This property is required if called by a service principal.",
            nullable=True,
        )
        _args_schema.communication_subject = AAZStrArg(
            options=["--communication-subject"],
            help="Subject of the communication.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.CommunicationsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.CommunicationsCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class CommunicationsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}/communications/{communicationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "communicationName", self.ctx.args.communication_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "supportTicketName", self.ctx.args.ticket_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-04-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_communication_details_read(cls._schema_on_200)

            return cls._schema_on_200

    class CommunicationsCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}/communications/{communicationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "communicationName", self.ctx.args.communication_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "supportTicketName", self.ctx.args.ticket_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-04-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_communication_details_read(cls._schema_on_200)

            return cls._schema_on_200

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("body", AAZStrType, ".communication_body", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("sender", AAZStrType, ".communication_sender")
                properties.set_prop("subject", AAZStrType, ".communication_subject", typ_kwargs={"flags": {"required": True}})

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_communication_details_read = None

    @classmethod
    def _build_schema_communication_details_read(cls, _schema):
        if cls._schema_communication_details_read is not None:
            _schema.id = cls._schema_communication_details_read.id
            _schema.name = cls._schema_communication_details_read.name
            _schema.properties = cls._schema_communication_details_read.properties
            _schema.type = cls._schema_communication_details_read.type
            return

        cls._schema_communication_details_read = _schema_communication_details_read = AAZObjectType()

        communication_details_read = _schema_communication_details_read
        communication_details_read.id = AAZStrType(
            flags={"read_only": True},
        )
        communication_details_read.name = AAZStrType(
            flags={"read_only": True},
        )
        communication_details_read.properties = AAZObjectType(
            flags={"required": True, "client_flatten": True},
        )
        communication_details_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_communication_details_read.properties
        properties.body = AAZStrType(
            flags={"required": True},
        )
        properties.communication_direction = AAZStrType(
            serialized_name="communicationDirection",
            flags={"read_only": True},
        )
        properties.communication_type = AAZStrType(
            serialized_name="communicationType",
            flags={"read_only": True},
        )
        properties.created_date = AAZStrType(
            serialized_name="createdDate",
            flags={"read_only": True},
        )
        properties.sender = AAZStrType()
        properties.subject = AAZStrType(
            flags={"required": True},
        )

        _schema.id = cls._schema_communication_details_read.id
        _schema.name = cls._schema_communication_details_read.name
        _schema.properties = cls._schema_communication_details_read.properties
        _schema.type = cls._schema_communication_details_read.type


__all__ = ["Update"]
