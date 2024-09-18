# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "apic environment create",
)
class Create(AAZCommand):
    """Create a new environment or update an existing environment.

    :example: Create environment
        az apic environment create -g api-center-test -n contosoeuap --environment-id public --title "Public cloud" --type "development"
    """

    _aaz_info = {
        "version": "2024-03-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.apicenter/services/{}/workspaces/{}/environments/{}", "2024-03-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.environment_id = AAZStrArg(
            options=["--environment-id"],
            help="The id of the environment.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.service_name = AAZStrArg(
            options=["-n", "--service-name"],
            help="The name of Azure API Center service.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["-w", "--workspace", "--workspace-name"],
            help="The name of the workspace.",
            required=True,
            default="default",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.custom_properties = AAZFreeFormDictArg(
            options=["--custom-properties"],
            arg_group="Properties",
            help="The custom metadata defined for API catalog entities.",
            blank={},
        )
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Properties",
            help="Environment description.",
        )
        _args_schema.type = AAZStrArg(
            options=["--type"],
            arg_group="Properties",
            help="Environment type.",
            required=True,
            enum={"development": "development", "production": "production", "staging": "staging", "testing": "testing"},
        )
        _args_schema.onboarding = AAZObjectArg(
            options=["--onboarding"],
            arg_group="Properties",
            help="Provide onboarding documentation related to your environment, e.g. {developerPortalUri:['https://developer.contoso.com'],instructions:'instructions markdown'}",
        )
        _args_schema.server = AAZObjectArg(
            options=["--server"],
            arg_group="Properties",
            help="Server information of the environment.",
        )
        _args_schema.title = AAZStrArg(
            options=["--title"],
            arg_group="Properties",
            help="Environment title.",
            required=True,
            fmt=AAZStrArgFormat(
                max_length=50,
                min_length=1,
            ),
        )

        onboarding = cls._args_schema.onboarding
        onboarding.developer_portal_uri = AAZListArg(
            options=["developer-portal-uri"],
            help="The location of the development portal",
        )
        onboarding.instructions = AAZStrArg(
            options=["instructions"],
            help="Onboarding guide.",
        )

        developer_portal_uri = cls._args_schema.onboarding.developer_portal_uri
        developer_portal_uri.Element = AAZStrArg()

        server = cls._args_schema.server
        server.management_portal_uri = AAZListArg(
            options=["management-portal-uri"],
            help="The location of the management portal",
        )
        server.type = AAZStrArg(
            options=["type"],
            help="Type of the server that represents the environment.",
            enum={"AWS API Gateway": "AWS API Gateway", "Apigee API Management": "Apigee API Management", "Azure API Management": "Azure API Management", "Azure compute service": "Azure compute service", "Kong API Gateway": "Kong API Gateway", "Kubernetes": "Kubernetes", "MuleSoft API Management": "MuleSoft API Management"},
        )

        management_portal_uri = cls._args_schema.server.management_portal_uri
        management_portal_uri.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.EnvironmentsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class EnvironmentsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiCenter/services/{serviceName}/workspaces/{workspaceName}/environments/{environmentName}",
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
                    "environmentName", self.ctx.args.environment_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "serviceName", self.ctx.args.service_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-03-01",
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
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("customProperties", AAZFreeFormDictType, ".custom_properties")
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_prop("kind", AAZStrType, ".type", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("onboarding", AAZObjectType, ".onboarding")
                properties.set_prop("server", AAZObjectType, ".server")
                properties.set_prop("title", AAZStrType, ".title", typ_kwargs={"flags": {"required": True}})

            custom_properties = _builder.get(".properties.customProperties")
            if custom_properties is not None:
                custom_properties.set_anytype_elements(".")

            onboarding = _builder.get(".properties.onboarding")
            if onboarding is not None:
                onboarding.set_prop("developerPortalUri", AAZListType, ".developer_portal_uri")
                onboarding.set_prop("instructions", AAZStrType, ".instructions")

            developer_portal_uri = _builder.get(".properties.onboarding.developerPortalUri")
            if developer_portal_uri is not None:
                developer_portal_uri.set_elements(AAZStrType, ".")

            server = _builder.get(".properties.server")
            if server is not None:
                server.set_prop("managementPortalUri", AAZListType, ".management_portal_uri")
                server.set_prop("type", AAZStrType, ".type")

            management_portal_uri = _builder.get(".properties.server.managementPortalUri")
            if management_portal_uri is not None:
                management_portal_uri.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.custom_properties = AAZFreeFormDictType(
                serialized_name="customProperties",
            )
            properties.description = AAZStrType()
            properties.kind = AAZStrType(
                flags={"required": True},
            )
            properties.onboarding = AAZObjectType()
            properties.server = AAZObjectType()
            properties.title = AAZStrType(
                flags={"required": True},
            )

            onboarding = cls._schema_on_200_201.properties.onboarding
            onboarding.developer_portal_uri = AAZListType(
                serialized_name="developerPortalUri",
            )
            onboarding.instructions = AAZStrType()

            developer_portal_uri = cls._schema_on_200_201.properties.onboarding.developer_portal_uri
            developer_portal_uri.Element = AAZStrType()

            server = cls._schema_on_200_201.properties.server
            server.management_portal_uri = AAZListType(
                serialized_name="managementPortalUri",
            )
            server.type = AAZStrType()

            management_portal_uri = cls._schema_on_200_201.properties.server.management_portal_uri
            management_portal_uri.Element = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
