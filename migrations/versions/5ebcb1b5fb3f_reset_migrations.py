"""reset migrations

Revision ID: 5ebcb1b5fb3f
Revises: None
Create Date: 2017-11-05 13:46:11.527506

"""

# revision identifiers, used by Alembic.
revision = '5ebcb1b5fb3f'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bank_account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sort_code', sa.String(), nullable=False),
    sa.Column('acct_id', sa.String(), nullable=False),
    sa.Column('currency', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bank_account'))
    )
    with op.batch_alter_table('bank_account', schema=None) as batch_op:
        batch_op.create_index('ix_bank_account_sort_code_acct_id', ['sort_code', 'acct_id'], unique=True)

    op.create_table('calendar_source',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('main_venue', sa.String(), nullable=True),
    sa.Column('contact_phone', sa.String(), nullable=True),
    sa.Column('contact_email', sa.String(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_calendar_source'))
    )
    op.create_table('cfp_vote_version',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('proposal_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('state', sa.String(), autoincrement=False, nullable=True),
    sa.Column('has_been_read', sa.Boolean(), autoincrement=False, nullable=True),
    sa.Column('created', sa.DateTime(), autoincrement=False, nullable=True),
    sa.Column('modified', sa.DateTime(), autoincrement=False, nullable=True),
    sa.Column('vote', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('note', sa.String(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'transaction_id', name=op.f('pk_cfp_vote_version'))
    )
    with op.batch_alter_table('cfp_vote_version', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_cfp_vote_version_operation_type'), ['operation_type'], unique=False)
        batch_op.create_index(batch_op.f('ix_cfp_vote_version_transaction_id'), ['transaction_id'], unique=False)

    op.create_table('email_job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(), nullable=False),
    sa.Column('text_body', sa.String(), nullable=False),
    sa.Column('html_body', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_email_job'))
    )
    op.create_table('favourite_proposals_version',
    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('proposal_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('transaction_id', name=op.f('pk_favourite_proposals_version'))
    )
    with op.batch_alter_table('favourite_proposals_version', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_favourite_proposals_version_operation_type'), ['operation_type'], unique=False)
        batch_op.create_index(batch_op.f('ix_favourite_proposals_version_transaction_id'), ['transaction_id'], unique=False)

    op.create_table('feature_flag',
    sa.Column('feature', sa.String(), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('feature', name=op.f('pk_feature_flag'))
    )
    op.create_table('permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_permission'))
    )
    with op.batch_alter_table('permission', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_permission_name'), ['name'], unique=True)

    op.create_table('product_group',
    sa.Column('capacity_max', sa.Integer(), nullable=True),
    sa.Column('capacity_used', sa.Integer(), nullable=True),
    sa.Column('expires', sa.DateTime(), nullable=True),
    sa.Column('attributes', sa.JSON(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['product_group.id'], name=op.f('fk_product_group_parent_id_product_group')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product_group')),
    sa.UniqueConstraint('name', name=op.f('uq_product_group_name'))
    )
    op.create_table('proposal_version',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('anonymiser_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('created', sa.DateTime(), autoincrement=False, nullable=True),
    sa.Column('modified', sa.DateTime(), autoincrement=False, nullable=True),
    sa.Column('state', sa.String(), autoincrement=False, nullable=True),
    sa.Column('type', sa.String(), autoincrement=False, nullable=True),
    sa.Column('title', sa.String(), autoincrement=False, nullable=True),
    sa.Column('description', sa.String(), autoincrement=False, nullable=True),
    sa.Column('requirements', sa.String(), autoincrement=False, nullable=True),
    sa.Column('length', sa.String(), autoincrement=False, nullable=True),
    sa.Column('notice_required', sa.String(), autoincrement=False, nullable=True),
    sa.Column('needs_help', sa.Boolean(), autoincrement=False, nullable=True),
    sa.Column('needs_money', sa.Boolean(), autoincrement=False, nullable=True),
    sa.Column('one_day', sa.Boolean(), autoincrement=False, nullable=True),
    sa.Column('has_rejected_email', sa.Boolean(), autoincrement=False, nullable=True),
    sa.Column('published_names', sa.String(), autoincrement=False, nullable=True),
    sa.Column('arrival_period', sa.String(), autoincrement=False, nullable=True),
    sa.Column('departure_period', sa.String(), autoincrement=False, nullable=True),
    sa.Column('telephone_number', sa.String(), autoincrement=False, nullable=True),
    sa.Column('may_record', sa.Boolean(), autoincrement=False, nullable=True),
    sa.Column('needs_laptop', sa.Boolean(), autoincrement=False, nullable=True),
    sa.Column('available_times', sa.String(), autoincrement=False, nullable=True),
    sa.Column('allowed_venues', sa.String(), autoincrement=False, nullable=True),
    sa.Column('allowed_times', sa.String(), autoincrement=False, nullable=True),
    sa.Column('scheduled_duration', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('scheduled_time', sa.DateTime(), autoincrement=False, nullable=True),
    sa.Column('scheduled_venue', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('potential_time', sa.DateTime(), autoincrement=False, nullable=True),
    sa.Column('potential_venue', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('attendees', sa.String(), autoincrement=False, nullable=True),
    sa.Column('cost', sa.String(), autoincrement=False, nullable=True),
    sa.Column('size', sa.String(), autoincrement=False, nullable=True),
    sa.Column('funds', sa.String(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'transaction_id', name=op.f('pk_proposal_version'))
    )
    with op.batch_alter_table('proposal_version', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_proposal_version_operation_type'), ['operation_type'], unique=False)
        batch_op.create_index(batch_op.f('ix_proposal_version_transaction_id'), ['transaction_id'], unique=False)

    op.create_table('purchase_version',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('type', sa.String(), autoincrement=False, nullable=True),
    sa.Column('owner_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('purchaser_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('price_tier_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('price_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('payment_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('refund_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('created', sa.DateTime(), autoincrement=False, nullable=True),
    sa.Column('modified', sa.DateTime(), autoincrement=False, nullable=True),
    sa.Column('state', sa.String(), autoincrement=False, nullable=True),
    sa.Column('expires', sa.DateTime(), autoincrement=False, nullable=True),
    sa.Column('checked_in', sa.Boolean(), autoincrement=False, nullable=True),
    sa.Column('badge_issued', sa.Boolean(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'transaction_id', name=op.f('pk_purchase_version'))
    )
    with op.batch_alter_table('purchase_version', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_purchase_version_operation_type'), ['operation_type'], unique=False)
        batch_op.create_index(batch_op.f('ix_purchase_version_transaction_id'), ['transaction_id'], unique=False)

    op.create_table('site_state',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('name', name=op.f('pk_site_state'))
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('will_have_ticket', sa.Boolean(), nullable=False),
    sa.Column('checkin_note', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user'))
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_name'), ['name'], unique=False)

    op.create_table('venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_venue')),
    sa.UniqueConstraint('name', name='_venue_name_uniq')
    )
    op.create_table('calendar_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(), nullable=True),
    sa.Column('start_dt', sa.DateTime(), nullable=False),
    sa.Column('end_dt', sa.DateTime(), nullable=False),
    sa.Column('source_id', sa.Integer(), nullable=False),
    sa.Column('summary', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['source_id'], ['calendar_source.id'], name=op.f('fk_calendar_event_source_id_calendar_source')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_calendar_event')),
    sa.UniqueConstraint('source_id', 'uid', name=op.f('uq_calendar_event_source_id'))
    )
    with op.batch_alter_table('calendar_event', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_calendar_event_source_id'), ['source_id'], unique=False)

    op.create_table('diversity',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('age', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('ethnicity', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_diversity_user_id_user')),
    sa.PrimaryKeyConstraint('user_id', name=op.f('pk_diversity'))
    )
    op.create_table('email_recipient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('sent', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['email_job.id'], name=op.f('fk_email_recipient_job_id_email_job')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_email_recipient_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_email_recipient'))
    )
    op.create_table('payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('provider', sa.String(), nullable=False),
    sa.Column('currency', sa.String(), nullable=False),
    sa.Column('amount_int', sa.Integer(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('reminder_sent', sa.Boolean(), nullable=False),
    sa.Column('bankref', sa.String(), nullable=True),
    sa.Column('gcid', sa.String(), nullable=True),
    sa.Column('chargeid', sa.String(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_payment_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_payment')),
    sa.UniqueConstraint('bankref', name=op.f('uq_payment_bankref')),
    sa.UniqueConstraint('chargeid', name=op.f('uq_payment_chargeid')),
    sa.UniqueConstraint('gcid', name=op.f('uq_payment_gcid'))
    )
    op.create_table('product',
    sa.Column('capacity_max', sa.Integer(), nullable=True),
    sa.Column('capacity_used', sa.Integer(), nullable=True),
    sa.Column('expires', sa.DateTime(), nullable=True),
    sa.Column('attributes', sa.JSON(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('display_name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['product_group.id'], name=op.f('fk_product_parent_id_product_group')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product'))
    )
    op.create_table('proposal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('anonymiser_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('requirements', sa.String(), nullable=True),
    sa.Column('length', sa.String(), nullable=True),
    sa.Column('notice_required', sa.String(), nullable=True),
    sa.Column('needs_help', sa.Boolean(), nullable=False),
    sa.Column('needs_money', sa.Boolean(), nullable=False),
    sa.Column('one_day', sa.Boolean(), nullable=False),
    sa.Column('has_rejected_email', sa.Boolean(), nullable=False),
    sa.Column('published_names', sa.String(), nullable=True),
    sa.Column('arrival_period', sa.String(), nullable=True),
    sa.Column('departure_period', sa.String(), nullable=True),
    sa.Column('telephone_number', sa.String(), nullable=True),
    sa.Column('may_record', sa.Boolean(), nullable=True),
    sa.Column('needs_laptop', sa.Boolean(), nullable=True),
    sa.Column('available_times', sa.String(), nullable=True),
    sa.Column('allowed_venues', sa.String(), nullable=True),
    sa.Column('allowed_times', sa.String(), nullable=True),
    sa.Column('scheduled_duration', sa.Integer(), nullable=True),
    sa.Column('scheduled_time', sa.DateTime(), nullable=True),
    sa.Column('scheduled_venue', sa.Integer(), nullable=True),
    sa.Column('potential_time', sa.DateTime(), nullable=True),
    sa.Column('potential_venue', sa.Integer(), nullable=True),
    sa.Column('attendees', sa.String(), nullable=True),
    sa.Column('cost', sa.String(), nullable=True),
    sa.Column('size', sa.String(), nullable=True),
    sa.Column('funds', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['anonymiser_id'], ['user.id'], name=op.f('fk_proposal_anonymiser_id_user')),
    sa.ForeignKeyConstraint(['potential_venue'], ['venue.id'], name=op.f('fk_proposal_potential_venue_venue')),
    sa.ForeignKeyConstraint(['scheduled_venue'], ['venue.id'], name=op.f('fk_proposal_scheduled_venue_venue')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_proposal_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_proposal'))
    )
    op.create_table('transaction',
    sa.Column('issued_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('remote_addr', sa.String(length=50), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_transaction_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_transaction'))
    )
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_transaction_user_id'), ['user_id'], unique=False)

    op.create_table('user_permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('permission_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['permission.id'], name=op.f('fk_user_permission_permission_id_permission')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_user_permission_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user_permission'))
    )
    with op.batch_alter_table('user_permission', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_permission_user_id'), ['user_id'], unique=False)

    op.create_table('bank_transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('posted', sa.DateTime(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('amount_int', sa.Integer(), nullable=False),
    sa.Column('fit_id', sa.String(), nullable=True),
    sa.Column('payee', sa.String(), nullable=False),
    sa.Column('payment_id', sa.Integer(), nullable=True),
    sa.Column('suppressed', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['bank_account.id'], name=op.f('fk_bank_transaction_account_id_bank_account')),
    sa.ForeignKeyConstraint(['payment_id'], ['payment.id'], name=op.f('fk_bank_transaction_payment_id_payment')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bank_transaction'))
    )
    with op.batch_alter_table('bank_transaction', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_bank_transaction_fit_id'), ['fit_id'], unique=False)
        batch_op.create_index('ix_bank_transaction_u1', ['account_id', 'posted', 'type', 'amount_int', 'payee', 'fit_id'], unique=True)

    op.create_table('cfp_message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('from_user_id', sa.Integer(), nullable=False),
    sa.Column('proposal_id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('is_to_admin', sa.Boolean(), nullable=True),
    sa.Column('has_been_read', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['from_user_id'], ['user.id'], name=op.f('fk_cfp_message_from_user_id_user')),
    sa.ForeignKeyConstraint(['proposal_id'], ['proposal.id'], name=op.f('fk_cfp_message_proposal_id_proposal')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cfp_message'))
    )
    op.create_table('cfp_vote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('proposal_id', sa.Integer(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('has_been_read', sa.Boolean(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('vote', sa.Integer(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['proposal_id'], ['proposal.id'], name=op.f('fk_cfp_vote_proposal_id_proposal')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_cfp_vote_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cfp_vote'))
    )
    with op.batch_alter_table('cfp_vote', schema=None) as batch_op:
        batch_op.create_index('ix_cfp_vote_user_id_proposal_id', ['user_id', 'proposal_id'], unique=True)

    op.create_table('favourite_calendar_events',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['calendar_event.id'], name=op.f('fk_favourite_calendar_events_event_id_calendar_event')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_favourite_calendar_events_user_id_user'))
    )
    op.create_table('favourite_proposals',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('proposal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['proposal_id'], ['proposal.id'], name=op.f('fk_favourite_proposals_proposal_id_proposal')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_favourite_proposals_user_id_user'))
    )
    op.create_table('payment_change',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('payment_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['payment_id'], ['payment.id'], name=op.f('fk_payment_change_payment_id_payment')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_payment_change'))
    )
    op.create_table('price_tier',
    sa.Column('capacity_max', sa.Integer(), nullable=True),
    sa.Column('capacity_used', sa.Integer(), nullable=True),
    sa.Column('expires', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=False),
    sa.Column('personal_limit', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['product.id'], name=op.f('fk_price_tier_parent_id_product')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_price_tier'))
    )
    op.create_table('refund',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('payment_id', sa.Integer(), nullable=False),
    sa.Column('provider', sa.String(), nullable=False),
    sa.Column('amount_int', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('refundid', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['payment_id'], ['payment.id'], name=op.f('fk_refund_payment_id_payment')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_refund')),
    sa.UniqueConstraint('refundid', name=op.f('uq_refund_refundid'))
    )
    op.create_table('stripe_refund',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('refundid', sa.String(), nullable=True),
    sa.Column('payment_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['payment_id'], ['payment.id'], name=op.f('fk_stripe_refund_payment_id_payment')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_stripe_refund')),
    sa.UniqueConstraint('refundid', name=op.f('uq_stripe_refund_refundid'))
    )
    op.create_table('product_price',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price_tier_id', sa.Integer(), nullable=False),
    sa.Column('currency', sa.String(), nullable=False),
    sa.Column('price_int', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['price_tier_id'], ['price_tier.id'], name=op.f('fk_product_price_price_tier_id_price_tier')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product_price'))
    )
    op.create_table('purchase',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('purchaser_id', sa.Integer(), nullable=False),
    sa.Column('price_tier_id', sa.Integer(), nullable=False),
    sa.Column('price_id', sa.Integer(), nullable=True),
    sa.Column('payment_id', sa.Integer(), nullable=True),
    sa.Column('refund_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('expires', sa.DateTime(), nullable=False),
    sa.Column('checked_in', sa.Boolean(), nullable=True),
    sa.Column('badge_issued', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], name=op.f('fk_purchase_owner_id_user')),
    sa.ForeignKeyConstraint(['payment_id'], ['payment.id'], name=op.f('fk_purchase_payment_id_payment')),
    sa.ForeignKeyConstraint(['price_id'], ['product_price.id'], name=op.f('fk_purchase_price_id_product_price')),
    sa.ForeignKeyConstraint(['price_tier_id'], ['price_tier.id'], name=op.f('fk_purchase_price_tier_id_price_tier')),
    sa.ForeignKeyConstraint(['purchaser_id'], ['user.id'], name=op.f('fk_purchase_purchaser_id_user')),
    sa.ForeignKeyConstraint(['refund_id'], ['refund.id'], name=op.f('fk_purchase_refund_id_refund')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_purchase'))
    )
    op.create_table('purchase_transfer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('purchase_id', sa.Integer(), nullable=False),
    sa.Column('to_user_id', sa.Integer(), nullable=False),
    sa.Column('from_user_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['from_user_id'], ['user.id'], name=op.f('fk_purchase_transfer_from_user_id_user')),
    sa.ForeignKeyConstraint(['purchase_id'], ['purchase.id'], name=op.f('fk_purchase_transfer_purchase_id_purchase')),
    sa.ForeignKeyConstraint(['to_user_id'], ['user.id'], name=op.f('fk_purchase_transfer_to_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_purchase_transfer'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('purchase_transfer')
    op.drop_table('purchase')
    op.drop_table('product_price')
    op.drop_table('stripe_refund')
    op.drop_table('refund')
    op.drop_table('price_tier')
    op.drop_table('payment_change')
    op.drop_table('favourite_proposals')
    op.drop_table('favourite_calendar_events')
    with op.batch_alter_table('cfp_vote', schema=None) as batch_op:
        batch_op.drop_index('ix_cfp_vote_user_id_proposal_id')

    op.drop_table('cfp_vote')
    op.drop_table('cfp_message')
    with op.batch_alter_table('bank_transaction', schema=None) as batch_op:
        batch_op.drop_index('ix_bank_transaction_u1')
        batch_op.drop_index(batch_op.f('ix_bank_transaction_fit_id'))

    op.drop_table('bank_transaction')
    with op.batch_alter_table('user_permission', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_permission_user_id'))

    op.drop_table('user_permission')
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_transaction_user_id'))

    op.drop_table('transaction')
    op.drop_table('proposal')
    op.drop_table('product')
    op.drop_table('payment')
    op.drop_table('email_recipient')
    op.drop_table('diversity')
    with op.batch_alter_table('calendar_event', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_calendar_event_source_id'))

    op.drop_table('calendar_event')
    op.drop_table('venue')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_name'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    op.drop_table('site_state')
    with op.batch_alter_table('purchase_version', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_purchase_version_transaction_id'))
        batch_op.drop_index(batch_op.f('ix_purchase_version_operation_type'))

    op.drop_table('purchase_version')
    with op.batch_alter_table('proposal_version', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_proposal_version_transaction_id'))
        batch_op.drop_index(batch_op.f('ix_proposal_version_operation_type'))

    op.drop_table('proposal_version')
    op.drop_table('product_group')
    with op.batch_alter_table('permission', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_permission_name'))

    op.drop_table('permission')
    op.drop_table('feature_flag')
    with op.batch_alter_table('favourite_proposals_version', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_favourite_proposals_version_transaction_id'))
        batch_op.drop_index(batch_op.f('ix_favourite_proposals_version_operation_type'))

    op.drop_table('favourite_proposals_version')
    op.drop_table('email_job')
    with op.batch_alter_table('cfp_vote_version', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_cfp_vote_version_transaction_id'))
        batch_op.drop_index(batch_op.f('ix_cfp_vote_version_operation_type'))

    op.drop_table('cfp_vote_version')
    op.drop_table('calendar_source')
    with op.batch_alter_table('bank_account', schema=None) as batch_op:
        batch_op.drop_index('ix_bank_account_sort_code_acct_id')

    op.drop_table('bank_account')
    # ### end Alembic commands ###
