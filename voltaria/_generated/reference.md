# Reference
## Clients
<details><summary><code>client.clients.<a href="src/voltaria_sdk/clients/client.py">list_clients</a>(...) -> PaginatedResponseClientResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of all clients associated with your partner account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.clients.list_clients()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by, e.g., 'created_at:desc,updated_at:asc'
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, name, correlation_id, company_number, status. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/voltaria_sdk/clients/client.py">create_client</a>(...) -> ClientResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new client under your partner account. The client will remain in a pending state until reviewed by Winyield.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.clients.create_client(
    name="ACME Corp",
    jurisdiction="eu",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the client
    
</dd>
</dl>

<dl>
<dd>

**jurisdiction:** `JurisdictionEnum` — The jurisdiction of the client, must be one of `eu`, `us`, `uk`
    
</dd>
</dl>

<dl>
<dd>

**correlation_id:** `typing.Optional[str]` — The correlation ID you provided at the creation of the client
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ClientTypeEnum]` — The type of the client, must be one of `individual`,`corporate`. Default is `corporate` if not provided.
    
</dd>
</dl>

<dl>
<dd>

**company_number:** `typing.Optional[str]` — The company number of the client if type is `corporate`
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[typing.Dict[str, typing.Any]]` — Additional data associated with the client
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/voltaria_sdk/clients/client.py">create_client_data</a>(...) -> ClientDataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload supplementary client information, such as bank account balance, accounting figures, or other relevant details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.clients.create_client_data(
    client_id="client_123",
    data={
        "key1": "value1",
        "key2": "value2"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/voltaria_sdk/clients/client.py">list_limit_requests</a>(...) -> PaginatedResponseLimitRequestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of all limit requests associated with your partner account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.clients.list_limit_requests()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Filter by client ID
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by, e.g., 'created_at:desc,updated_at:asc'
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, client_id. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/voltaria_sdk/clients/client.py">create_limit_request</a>(...) -> LimitRequestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a limit review request for a client. The request will remain in a pending state until reviewed by Winyield.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.clients.create_limit_request(
    client_id="client_1234567890abcdef",
    requested_limit=1.1,
    reason="Need more credit for business expansion",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — The ID of the client for which the limit request is being created
    
</dd>
</dl>

<dl>
<dd>

**requested_limit:** `LimitRequestCreatePayloadRequestedLimit` — The requested credit limit amount
    
</dd>
</dl>

<dl>
<dd>

**reason:** `str` — The reason for the limit request
    
</dd>
</dl>

<dl>
<dd>

**waiver_request:** `typing.Optional[bool]` — Whether a special waiver is requested alongside this limit request
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/voltaria_sdk/clients/client.py">get_limit_request</a>(...) -> LimitRequestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific limit request by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.clients.get_limit_request(
    request_id="request_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/voltaria_sdk/clients/client.py">list_onboarding_clients</a>(...) -> PaginatedResponseClientResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all clients that have self-registered via the portal and are awaiting partner approval.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.clients.list_onboarding_clients()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/voltaria_sdk/clients/client.py">approve_onboarding</a>(...) -> ClientResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Accept a self-onboarded client. The client status moves to 'pending' and the owner's portal account is activated so they can begin submitting documents.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.clients.approve_onboarding(
    client_id="client_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/voltaria_sdk/clients/client.py">reject_onboarding</a>(...) -> ClientResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reject a self-onboarded client. The client record is kept with 'rejected' status for audit history and is not deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.clients.reject_onboarding(
    client_id="client_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/voltaria_sdk/clients/client.py">list_client_portal_users</a>(...) -> PaginatedResponseClientUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Paginated list of portal users belonging to a client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.clients.list_client_portal_users(
    client_id="client_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, email, status, first_name, last_name. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/voltaria_sdk/clients/client.py">add_client_portal_user</a>(...) -> ClientUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invite a new user to a client's portal account. The invited user will receive an email with a one-time link to set their password. Partner can assign any role: 'owner', 'admin', or 'viewer'.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.clients.add_client_portal_user(
    client_id="client_id",
    first_name="first_name",
    last_name="last_name",
    email="email",
    role_type="role_type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**role_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/voltaria_sdk/clients/client.py">list_client_waivers</a>(...) -> PaginatedResponseWaiverResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all waivers associated with a specific client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.clients.list_client_waivers(
    client_id="client_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by, e.g., 'created_at:desc'
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, client_id, status. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/voltaria_sdk/clients/client.py">get_client_by_id</a>(...) -> ClientResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed information for a specific client using their client ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.clients.get_client_by_id(
    client_id="client_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/voltaria_sdk/clients/client.py">delete_client</a>(...) -> typing.Optional[typing.Dict[str, typing.Any]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a client by ID. Only clients with 'pending' status can be deleted. All client's loans must also be in 'pending' status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.clients.delete_client(
    client_id="client_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/voltaria_sdk/clients/client.py">list_client_checklist_summaries</a>(...) -> PaginatedResponseChecklistSummaryPartnerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the checklist summaries for one of your clients, including the AI description and item completion counts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.clients.list_client_checklist_summaries(
    client_id="client_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sandbox
<details><summary><code>client.sandbox.<a href="src/voltaria_sdk/sandbox/client.py">update_client</a>(...) -> ClientResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing client's status or credit limit using their client ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.sandbox.update_client(
    client_id="client_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ClientStatusEnum]` — The status of the client. One of the following: `active, rejected, deactivated, pending, pending_onboarding, pre_approved, deleted, inactive`
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[ClientUpdateSandboxLimit]` — The limit to set for the client. This will override the existing limit.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandbox.<a href="src/voltaria_sdk/sandbox/client.py">update_loan</a>(...) -> LoanResponseWithInstallments</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the status of a specific loan using its unique loan ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.sandbox.update_loan(
    loan_id="loan_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**loan_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[LoanStatusEnum]` — The status of the client. One of the following: `pending, overdue, active, default, sold, restructured, repaid, pre_approved, rejected, deleted, inactive`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandbox.<a href="src/voltaria_sdk/sandbox/client.py">webhook_test</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Test a webhook subscription by ID or trigger all by event type.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.sandbox.webhook_test(
    event_type="loan.updated",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_type:** `WebhookEventTypeEnum` — Event type to trigger for the test. All subscriptions for this event type will be triggered if webhook_id is not provided.Possible values: loan_updated, installment_updated, client_updated, client_limit_updated, partner_limit_updated
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `typing.Optional[str]` — The ID of the webhook subscription. Only this webhook will be triggered if provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Accounts
<details><summary><code>client.accounts.<a href="src/voltaria_sdk/accounts/client.py">list_client_account_fields</a>(...) -> typing.Dict[str, CurrencyFieldSpec]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the required and optional bank account fields for each supported currency. Fetch once and cache; use it to build the create-account request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.accounts.list_client_account_fields(
    client_id="client_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/voltaria_sdk/accounts/client.py">list_client_accounts</a>(...) -> PaginatedResponseClientAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all bank accounts for one of your clients.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.accounts.list_client_accounts(
    client_id="client_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/voltaria_sdk/accounts/client.py">create_client_account</a>(...) -> ClientAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a bank account for one of your clients. The account is registered with the payment provider immediately. Use the `status` field to create it as `active` (default; demotes any existing active account in the same currency to `passive`) or `passive`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.accounts.create_client_account(
    client_id="client_id",
    account_holder_name="Acme Ltd",
    account_holder_type="business",
    currency="gbp",
    sort_code="40-47-84",
    account_number="12345678",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**account_holder_name:** `str` — Full name of the account holder.
    
</dd>
</dl>

<dl>
<dd>

**account_holder_type:** `AccountHolderTypeEnum` — Account holder type. One of: `business`, `private`.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `CurrencyEnum` — ISO 4217 currency code. Use `/accounts/fields` to get required fields per currency.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Optional label / nickname for the account (max 50 characters).
    
</dd>
</dl>

<dl>
<dd>

**sort_code:** `typing.Optional[str]` — Sort code (required for GBP).
    
</dd>
</dl>

<dl>
<dd>

**account_number:** `typing.Optional[str]` — Account number (required for GBP and USD).
    
</dd>
</dl>

<dl>
<dd>

**iban:** `typing.Optional[str]` — IBAN (required for EUR, CZK, PLN).
    
</dd>
</dl>

<dl>
<dd>

**bic:** `typing.Optional[str]` — BIC / SWIFT code (optional for EUR).
    
</dd>
</dl>

<dl>
<dd>

**routing_number:** `typing.Optional[str]` — ABA routing number (required for USD).
    
</dd>
</dl>

<dl>
<dd>

**account_type:** `typing.Optional[str]` — Account type (required for USD). E.g. `checking` or `savings`.
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[AccountAddress]` — Account holder address (required for USD).
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PartnerClientAccountCreateRequestStatus]` — Account status. `active` demotes any existing active account in the same currency to `passive`; `passive` is added as a backup. Defaults to `active`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/voltaria_sdk/accounts/client.py">get_client_account</a>(...) -> ClientAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific bank account for one of your clients.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.accounts.get_client_account(
    client_id="client_id",
    account_id="account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Collections
<details><summary><code>client.collections.<a href="src/voltaria_sdk/collections/client.py">list_collection_actions</a>(...) -> PaginatedResponseCollectionActionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all collection actions configured for your partner account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.collections.list_collection_actions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by, e.g., 'created_at:desc,updated_at:asc'
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, name, action_type, is_active, timing. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/voltaria_sdk/collections/client.py">list_collection_action_logs</a>(...) -> PaginatedResponseCollectionActionLogResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve collection action logs for your partner account. Supports filtering by client, loan, installment, status, or action type.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.collections.list_collection_action_logs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**loan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**installment_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[CollectionActionStatusEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**action_type:** `typing.Optional[CollectionActionTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by, e.g., 'created_at:desc,updated_at:asc'
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, collection_action_id, action_type, status, client_id, loan_id, installment_id, scheduled_for. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/voltaria_sdk/collections/client.py">update_collection_action_log</a>(...) -> CollectionActionLogResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the status and notes of a collection action log.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.collections.update_collection_action_log(
    log_id="log_id",
    status="completed",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**log_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `CollectionActionLogUpdatePayloadStatus` — The updated status of the action: 'completed' or 'failed'
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes about this action
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Documents
<details><summary><code>client.documents.<a href="src/voltaria_sdk/documents/client.py">list_documents</a>(...) -> PaginatedResponseDocumentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all documents linked to a client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.documents.list_documents()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**loan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**installment_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**waterfall_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by, e.g., 'created_at:desc,updated_at:asc'
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, client_id, loan_id, installment_id, waterfall_id, category, file_name, document_date, folder_path. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/voltaria_sdk/documents/client.py">upload_document</a>(...) -> DocumentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a new document related to a client or loan, such as financial statements or KYC files.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.documents.upload_document(
    file="example_file",
    category="category",
    file_name="file_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category:** `str` — The category of the document. Available options can be fetched from the available categories endpoint. '.../documents/available-categories'.
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` — The name of the file
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` — The file to upload
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**loan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**installment_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**waterfall_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/voltaria_sdk/documents/client.py">get_available_document_categories</a>() -> AvailableDocumentCategoriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all available document categories.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.documents.get_available_document_categories()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/voltaria_sdk/documents/client.py">get_document_by_id</a>(...) -> DocumentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details for a specific document using its document ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.documents.get_document_by_id(
    document_id="document_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/voltaria_sdk/documents/client.py">delete_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific document by using its document ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.documents.delete_document(
    document_id="document_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Investors
<details><summary><code>client.investors.<a href="src/voltaria_sdk/investors/client.py">investor_list_clients</a>(...) -> PaginatedResponseClientInvestorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all clients with at least one loan funded by this investor.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.investors.investor_list_clients()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, name, correlation_id, company_number, status. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.investors.<a href="src/voltaria_sdk/investors/client.py">investor_get_client</a>(...) -> ClientInvestorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific client that has a loan funded by this investor.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.investors.investor_get_client(
    client_id="client_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.investors.<a href="src/voltaria_sdk/investors/client.py">investor_list_loans</a>(...) -> PaginatedResponseLoanInvestorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all loans funded by the current investor.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.investors.investor_list_loans()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, partner_id, client_id, status, loan_date, currency, partner.name, client.name. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.investors.<a href="src/voltaria_sdk/investors/client.py">investor_get_loan</a>(...) -> LoanResponseWithInstallments</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific loan funded by the current investor, with its installments.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.investors.investor_get_loan(
    loan_id="loan_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**loan_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.investors.<a href="src/voltaria_sdk/investors/client.py">investor_list_installments</a>(...) -> PaginatedResponseInstallmentResponseWithClientInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all installments for loans funded by the current investor.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.investors.investor_list_installments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**loan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, client_id, loan_id, status, client.name, expected_repayment_at. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.investors.<a href="src/voltaria_sdk/investors/client.py">investor_get_installment</a>(...) -> InstallmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific installment for a loan funded by the current investor.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.investors.investor_get_installment(
    installment_id="installment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**installment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.investors.<a href="src/voltaria_sdk/investors/client.py">investor_list_repayments</a>(...) -> PaginatedResponseRepaymentResponseWithClientInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all repayment logs for loans funded by the current investor.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.investors.investor_list_repayments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**loan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**installment_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, client_id, loan_id, installment_id, created_at, client.name, client.correlation_id. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Installments
<details><summary><code>client.installments.<a href="src/voltaria_sdk/installments/client.py">list_installments</a>(...) -> PaginatedResponseInstallmentResponseWithClientInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of all loan installments under your partner account. Supports optional filtering by loan or client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.installments.list_installments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**loan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by, e.g., 'created_at:desc,updated_at:asc'
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, client_id, loan_id, status, client.name, expected_repayment_at. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.installments.<a href="src/voltaria_sdk/installments/client.py">add_installment</a>(...) -> typing.List[InstallmentResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add new installments to a loan with its specific loan ID. This endpoint is available to select partners and will trigger the recalculation of the IRR and interest amounts for all installments of the loan.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria, LoanInstallmentCreatePayload
from voltaria_sdk.environment import VoltariaEnvironment
import datetime

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.installments.add_installment(
    loan_id="loan_12345",
    installments=[
        LoanInstallmentCreatePayload(
            expected_repayment_at=datetime.date.fromisoformat("2025-12-01"),
            amount="1000.00",
        ),
        LoanInstallmentCreatePayload(
            expected_repayment_at=datetime.date.fromisoformat("2026-01-01"),
            amount="1000.00",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**loan_id:** `str` — The loan ID to add the installments to
    
</dd>
</dl>

<dl>
<dd>

**installments:** `typing.List[LoanInstallmentCreatePayload]` — List of installments to add to the loan
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.installments.<a href="src/voltaria_sdk/installments/client.py">list_payment_promises</a>(...) -> PaginatedResponsePaymentPromiseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of payment promises recorded for installments under your partner account. Supports optional filtering by loan or client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.installments.list_payment_promises()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by, e.g., 'created_at:desc,updated_at:asc'
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, installment_id, status, promised_date, created_at. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**loan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.installments.<a href="src/voltaria_sdk/installments/client.py">create_payment_promise</a>(...) -> PaymentPromiseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Record a payment promise made by a client for one of their installments. The promised date must be today or in the future.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment
import datetime

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.installments.create_payment_promise(
    installment_id="inst_12345",
    amount=1.1,
    promised_date=datetime.date.fromisoformat("2026-05-15"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**installment_id:** `str` — The ID of the installment this promise relates to
    
</dd>
</dl>

<dl>
<dd>

**amount:** `PaymentPromiseCreatePayloadAmount` — The amount the client has promised to pay (must be > 0)
    
</dd>
</dl>

<dl>
<dd>

**promised_date:** `datetime.date` — The date the client has committed to pay by (today or future)
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Optional notes captured during the collections interaction
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.installments.<a href="src/voltaria_sdk/installments/client.py">get_installment_by_id</a>(...) -> InstallmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed information for a specific installment using its installment ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.installments.get_installment_by_id(
    installment_id="installment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**installment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.installments.<a href="src/voltaria_sdk/installments/client.py">edit_installment</a>(...) -> InstallmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an installment's amount and expected repayment date with its specific installment ID. This endpoint is available to select partners and will trigger the recalculation of the IRR and interest amounts for all installments of the loan.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment
import datetime

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.installments.edit_installment(
    installment_id="installment_id",
    amount=1.1,
    expected_repayment_at=datetime.date.fromisoformat("2025-12-01"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**installment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `InstallmentEditPayloadAmount` — The new amount for the installment
    
</dd>
</dl>

<dl>
<dd>

**expected_repayment_at:** `datetime.date` — The new expected repayment date
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.installments.<a href="src/voltaria_sdk/installments/client.py">delete_installment</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an installment with its specific installment ID. This endpoint is available to select partners and will trigger the recalculation of the IRR and interest amounts for all installments of the loan.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.installments.delete_installment(
    installment_id="installment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**installment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Loans
<details><summary><code>client.loans.<a href="src/voltaria_sdk/loans/client.py">list_loan_review_requests</a>(...) -> PaginatedResponseLoanReviewRequestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List loan review requests for your partner account, optionally filtered by loan ID or client ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.loans.list_loan_review_requests()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**loan_id:** `typing.Optional[str]` — Filter by loan ID
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Filter by client ID
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by, e.g., 'created_at:desc,updated_at:asc'
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, loan_id, client_id, status. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loans.<a href="src/voltaria_sdk/loans/client.py">create_loan_review_request</a>(...) -> LoanReviewRequestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ask Voltaria to review a not-yet-disbursed (pending or pre-approved) loan before disbursement.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.loans.create_loan_review_request(
    loan_id="loan_1234567890abcdef",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**loan_id:** `str` — The ID of the loan to be reviewed. Must be a not-yet-disbursed (pending or pre-approved) loan belonging to the current partner
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Optional note from the requester explaining the review request
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loans.<a href="src/voltaria_sdk/loans/client.py">get_loan_review_request</a>(...) -> LoanReviewRequestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific loan review request by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.loans.get_loan_review_request(
    request_id="request_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loans.<a href="src/voltaria_sdk/loans/client.py">list_loans</a>(...) -> PaginatedResponseLoanResponseWithClientInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all loans associated with your partner account. Supports optional filtering by client ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.loans.list_loans()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by, e.g., 'created_at:desc,updated_at:asc'
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, client_id, status, client.name, correlation_id. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loans.<a href="src/voltaria_sdk/loans/client.py">create_loan</a>(...) -> LoanResponseWithInstallments</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new loan for an approved client with an active credit limit.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria, LoanInstallmentCreatePayload
from voltaria_sdk.environment import VoltariaEnvironment
import datetime

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.loans.create_loan(
    client_id="client_ACME",
    currency="eur",
    amount=1.1,
    installments=[
        LoanInstallmentCreatePayload(
            expected_repayment_at=datetime.date.fromisoformat("2025-12-01"),
            amount=1.1,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — The ID of the client for this loan
    
</dd>
</dl>

<dl>
<dd>

**currency:** `CurrencyEnum` — The currency of the loan, must be one of the supported currencies: eur, gbp, usd, czk, pln, isk
    
</dd>
</dl>

<dl>
<dd>

**amount:** `LoanCreatePayloadAmount` — The amount of the loan
    
</dd>
</dl>

<dl>
<dd>

**installments:** `typing.List[LoanInstallmentCreatePayload]` — List of installments for the loan, each with a due date and amount
    
</dd>
</dl>

<dl>
<dd>

**correlation_id:** `typing.Optional[str]` — The correlation ID you provided at the creation of the loan
    
</dd>
</dl>

<dl>
<dd>

**loan_date:** `typing.Optional[datetime.date]` — Please provide the loan_date if it differs from the loan creation time (created_at). Otherwise, it will be automatically set.
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[typing.Dict[str, typing.Any]]` — Additional data related to the loan
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loans.<a href="src/voltaria_sdk/loans/client.py">get_loan_by_id</a>(...) -> LoanResponseWithInstallments</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed information about a specific loan by its loan ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.loans.get_loan_by_id(
    loan_id="loan_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**loan_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loans.<a href="src/voltaria_sdk/loans/client.py">delete_loan</a>(...) -> typing.Optional[typing.Dict[str, typing.Any]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a loan by ID. Only loans with 'pending' status can be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.loans.delete_loan(
    loan_id="loan_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**loan_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loans.<a href="src/voltaria_sdk/loans/client.py">create_bulk_loans</a>(...) -> BulkLoanTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create multiple loans in a single request. Processing happens asynchronously. Returns a task ID for tracking progress.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria, BulkLoanItemPayload, LoanInstallmentCreatePayload
from voltaria_sdk.environment import VoltariaEnvironment
import datetime

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.loans.create_bulk_loans(
    loans=[
        BulkLoanItemPayload(
            client_id="client_123",
            currency="eur",
            amount="50000.00",
            correlation_id="LOAN_001",
            loan_date=datetime.date.fromisoformat("2023-05-01"),
            installments=[
                LoanInstallmentCreatePayload(
                    expected_repayment_at=datetime.date.fromisoformat("2023-06-01"),
                    amount="26000.00",
                ),
                LoanInstallmentCreatePayload(
                    expected_repayment_at=datetime.date.fromisoformat("2023-07-01"),
                    amount="26000.00",
                )
            ],
            data={
                "loan_type": "business",
                "purpose": "expansion"
            },
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**loans:** `typing.List[BulkLoanItemPayload]` — List of loans to create (max 1000)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loans.<a href="src/voltaria_sdk/loans/client.py">get_bulk_loan_status</a>(...) -> BulkLoanTaskStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the status of a bulk loan creation task and retrieve results when completed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.loans.get_bulk_loan_status(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loans.<a href="src/voltaria_sdk/loans/client.py">set_loan_default</a>(...) -> LoanResponseWithInstallments</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark a loan as defaulted, recording the default date and the amount recovered from selling it. Defaults the loan's active and overdue installments and updates the loan status accordingly.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment
import datetime

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.loans.set_loan_default(
    loan_id="loan_id",
    default_date=datetime.date.fromisoformat("2026-06-23"),
    sold_amount=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**loan_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**default_date:** `datetime.date` — Date the loan is marked as defaulted.
    
</dd>
</dl>

<dl>
<dd>

**sold_amount:** `LoanDefaultPayloadSoldAmount` — Amount recovered when the defaulted loan is sold.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Partners
<details><summary><code>client.partners.<a href="src/voltaria_sdk/partners/client.py">get_available_funding</a>() -> typing.List[AvailableFunding]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this endpoint to check the available funding capacity in your dedicated lending account before initiating a new loan or submitting a drawdown request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.partners.get_available_funding()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partners.<a href="src/voltaria_sdk/partners/client.py">create_partner_data</a>(...) -> PartnerDataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload supplementary partner information, such as bank account balance, accounting figures, or other relevant details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.partners.create_partner_data(
    data={
        "key1": "value1",
        "key2": "value2"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partners.<a href="src/voltaria_sdk/partners/client.py">list_partner_waterfalls</a>(...) -> PaginatedResponseWaterfallResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this endpoint to get the list of waterfalls for your dedicated lending account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.partners.list_partner_waterfalls()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by, e.g., 'created_at:desc,updated_at:asc'
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, name, date, status, created_at, updated_at. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Recoveries
<details><summary><code>client.recoveries.<a href="src/voltaria_sdk/recoveries/client.py">list_recoveries</a>(...) -> PaginatedResponseRecoveryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve recoveries recorded against your loans. Supports filtering by client or loan.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.recoveries.list_recoveries()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**loan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by, e.g., 'created_at:desc,updated_at:asc'
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, client_id, loan_id, currency, recovery_date, created_at. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.recoveries.<a href="src/voltaria_sdk/recoveries/client.py">create_recovery</a>(...) -> RecoveryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Record a new recovery against one of your loans.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment
import datetime

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.recoveries.create_recovery(
    loan_id="loan_abc123",
    amount=1.1,
    currency="eur",
    recovery_date=datetime.date.fromisoformat("2026-07-15"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**loan_id:** `str` — The ID of the loan this recovery is associated with.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `RecoveryCreatePayloadAmount` — The amount recovered (must be > 0).
    
</dd>
</dl>

<dl>
<dd>

**currency:** `CurrencyEnum` — The currency of the recovered amount, must be one of the supported currencies: eur, gbp, usd, czk, pln, isk
    
</dd>
</dl>

<dl>
<dd>

**recovery_date:** `datetime.date` — The date the recovery was made.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Optional notes about the recovery.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks
<details><summary><code>client.webhooks.<a href="src/voltaria_sdk/webhooks/client.py">list_webhook_subscriptions</a>(...) -> PaginatedResponseWebhookSubscriptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all webhook subscriptions for your partner account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.webhooks.list_webhook_subscriptions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `typing.Optional[WebhookEventTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/voltaria_sdk/webhooks/client.py">create_webhook_subscription</a>(...) -> WebhookSubscriptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new webhook subscription for a specific event type.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.webhooks.create_webhook_subscription(
    url="https://example.com/webhooks",
    description="Loan update event",
    event_type="loan.updated",
    secret="whsec_f3o9p8h7g6j5k4l3m2n1o0p9i8u7y6t5",
    retry=False,
    status="active",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `str` — The URL to send webhooks to
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `WebhookEventTypeEnum` — Event type to subscribe toPossible values: loan_updated, installment_updated, client_updated, client_limit_updated, partner_limit_updated
    
</dd>
</dl>

<dl>
<dd>

**secret:** `str` — Secret for signing webhook payloads
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of this webhook endpoint
    
</dd>
</dl>

<dl>
<dd>

**retry:** `typing.Optional[bool]` — Whether to retry failed webhooks
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[WebhookStatusEnum]` — Status of the webhook subscription. Defaults to 'active'.Possible values: active, paused, disabled
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/voltaria_sdk/webhooks/client.py">get_webhook_subscription</a>(...) -> WebhookSubscriptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details for a specific webhook subscription with its webhook ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.webhooks.get_webhook_subscription(
    webhook_id="webhook_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/voltaria_sdk/webhooks/client.py">update_webhook_subscription</a>(...) -> WebhookSubscriptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a webhook subscription with its specific webhook ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.webhooks.update_webhook_subscription(
    webhook_id="webhook_id",
    url="https://example.com/webhooks/v2",
    description="Updated webhook endpoint",
    event_type="installment.updated",
    status="paused",
    retry=True,
    secret="whsec_updated_secret_here",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The URL to send webhooks to
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of this webhook endpoint
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `typing.Optional[WebhookEventTypeEnum]` — Event type to subscribe toPossible values: loan_updated, installment_updated, client_updated, client_limit_updated, partner_limit_updated
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[WebhookStatusEnum]` — Status of the webhook subscriptionPossible values: active, paused, disabled
    
</dd>
</dl>

<dl>
<dd>

**retry:** `typing.Optional[bool]` — Whether to retry failed webhooks
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` — Secret for signing webhook payloads
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/voltaria_sdk/webhooks/client.py">delete_webhook_subscription</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific webhook subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.webhooks.delete_webhook_subscription(
    webhook_id="webhook_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/voltaria_sdk/webhooks/client.py">list_webhook_logs</a>(...) -> PaginatedResponseWebhookLogResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all webhook logs linked to your partner account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.webhooks.list_webhook_logs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Repayments
<details><summary><code>client.repayments.<a href="src/voltaria_sdk/repayments/client.py">list_repayment_logs</a>(...) -> PaginatedResponseRepaymentResponseWithClientInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all repayments made under your partner account. Supports filtering by client, loan, or installments.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.repayments.list_repayment_logs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**loan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**installment_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by, e.g., 'created_at:desc,updated_at:asc'
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: id, client_id, loan_id, installment_id, created_at, client.name, client.correlation_id. Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.repayments.<a href="src/voltaria_sdk/repayments/client.py">create_repayment</a>(...) -> RepaymentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new repayment log for an installment. Requires the installment ID, loan ID or loan correlation ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.repayments.create_repayment(
    amount=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount:** `RepaymentCreatePayloadAmount` — The amount of payment made for installment
    
</dd>
</dl>

<dl>
<dd>

**installment_id:** `typing.Optional[str]` — ID of the installment
    
</dd>
</dl>

<dl>
<dd>

**loan_id:** `typing.Optional[str]` — ID of the associated Loan
    
</dd>
</dl>

<dl>
<dd>

**correlation_id:** `typing.Optional[str]` — Correlation ID of associated loan
    
</dd>
</dl>

<dl>
<dd>

**repayment_date:** `typing.Optional[datetime.datetime]` — Please provide the repayment_date if it differs from the time you log this repayment. Otherwise, it will be automatically set.
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[typing.Dict[str, typing.Any]]` — Additional metadata related to the repayment
    
</dd>
</dl>

<dl>
<dd>

**is_early_settlement:** `typing.Optional[bool]` — Indicates if this repayment is for early settlement
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.repayments.<a href="src/voltaria_sdk/repayments/client.py">create_bulk_repayments</a>(...) -> BulkRepaymentTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiate processing of up to 10000 repayment logs. Returns task_id for tracking progress.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria, BulkRepaymentItemPayload
from voltaria_sdk.environment import VoltariaEnvironment
import datetime

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.repayments.create_bulk_repayments(
    repayments=[
        BulkRepaymentItemPayload(
            amount="1000.00",
            repayment_date=datetime.datetime.fromisoformat("2023-10-01T12:00:00+00:00"),
            data={
                "reference": "TXN-001",
                "type": "transfer"
            },
            installment_id="installment_123",
        ),
        BulkRepaymentItemPayload(
            amount="500.50",
            data={
                "notes": "Payment received in office",
                "type": "cash"
            },
            loan_id="loan_456",
        ),
        BulkRepaymentItemPayload(
            amount="750.00",
            repayment_date=datetime.datetime.fromisoformat("2023-09-30T15:30:00+00:00"),
            correlation_id="LOAN-789",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**repayments:** `typing.List[BulkRepaymentItemPayload]` — List of repayments to create (max 10000)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.repayments.<a href="src/voltaria_sdk/repayments/client.py">get_bulk_repayment_status</a>(...) -> BulkRepaymentTaskStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the progress and results of a bulk repayment processing task.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.repayments.get_bulk_repayment_status(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Drawdowns
<details><summary><code>client.drawdowns.<a href="src/voltaria_sdk/drawdowns/client.py">list_drawdowns</a>(...) -> PaginatedResponseDrawdownResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of drawdowns.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.drawdowns.list_drawdowns()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by, e.g., 'created_at:desc,updated_at:asc'
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: . Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drawdowns.<a href="src/voltaria_sdk/drawdowns/client.py">create_drawdown_request</a>(...) -> DrawdownResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new drawdown request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.drawdowns.create_drawdown_request(
    amount=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount:** `DrawdownCreatePayloadAmount` — The amount for the drawdown.
    
</dd>
</dl>

<dl>
<dd>

**drawdown_date:** `typing.Optional[datetime.datetime]` — The date for the drawdown. If not provided, defaults to the current date and time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drawdowns.<a href="src/voltaria_sdk/drawdowns/client.py">list_drawdown_checklists</a>(...) -> PaginatedResponseDrawdownChecklistResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all checklist items for a specific drawdown
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from voltaria import Voltaria
from voltaria_sdk.environment import VoltariaEnvironment

client = Voltaria(
    token="<token>",
    environment=VoltariaEnvironment.SANDBOX,
)

client.drawdowns.list_drawdown_checklists(
    drawdown_id="drawdown_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**drawdown_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by, e.g., 'created_at:desc,updated_at:asc'
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query string for filtering. Format: "field:operator:value;...". Supported fields: . Supported operators: is, in, not_in, contains, not_contains, like, not_like, ilike, not_ilike, gt, gte, lt, lte, starts_with, ends_with, is_null, is_not_null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

