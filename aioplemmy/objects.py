import base64
from abc import ABC
from dataclasses import dataclass
from typing import Optional
from urllib.parse import urlparse


@dataclass
class _LemmyObject(ABC):
    id: int = None

    @property
    def id_b64_(self) -> str:
        return base64.urlsafe_b64encode(int.to_bytes(self.id, length=4, byteorder='little', signed=False)).rstrip(b'=A')\
            .decode("ascii")

    @staticmethod
    def b64_to_id(id_: str) -> int:
        id_ = id_.ljust(6, 'A') + '=='
        return int.from_bytes(base64.urlsafe_b64decode(id_), byteorder='little', signed=False)

@dataclass
class _InstanceBound(_LemmyObject):
    actor_id: str = None
    local: bool = None
    instance_id: int = None

    @property
    def instance_domain_(self) -> Optional[str]:
        return None if self.local else urlparse(self.actor_id).hostname

@dataclass
class AdminPurgeComment(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/AdminPurgeComment.html"""

    admin_person_id: int = None
    post_id: int = None
    reason: str = None
    when_: str = None


@dataclass
class AdminPurgeCommunity(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/AdminPurgeCommunity.html"""

    admin_person_id: int = None
    reason: str = None
    when_: str = None


@dataclass
class AdminPurgePerson(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/AdminPurgePerson.html"""

    admin_person_id: int = None
    reason: str = None
    when_: str = None


@dataclass
class AdminPurgePost(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/AdminPurgePost.html"""

    admin_person_id: int = None
    community_id: int = None
    reason: str = None
    when_: str = None


@dataclass
class CaptchaResponse:
    """https://join-lemmy.org/api/interfaces/CaptchaResponse.html"""

    png: str = None
    uuid: str = None
    wav: str = None


@dataclass
class Comment(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/Comment.html"""

    ap_id: str = None
    content: str = None
    creator_id: int = None
    deleted: bool = None
    distinguished: bool = None
    language_id: int = None
    local: bool = None
    path: str = None
    post_id: int = None
    published: str = None
    removed: bool = None
    updated: str = None


@dataclass
class CommentAggregates(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/CommentAggregates.html"""

    child_count: int = None
    comment_id: int = None
    downvotes: int = None
    hot_rank: int = None
    published: str = None
    score: int = None
    upvotes: int = None


@dataclass
class CommentReply(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/CommentReply.html"""

    comment_id: int = None
    published: str = None
    read: bool = None
    recipient_id: int = None


@dataclass
class CommentReport(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/CommentReport.html"""

    comment_id: int = None
    creator_id: int = None
    original_comment_text: str = None
    published: str = None
    reason: str = None
    resolved: bool = None
    resolver_id: int = None
    updated: str = None


@dataclass
class Community(_InstanceBound):
    """https://join-lemmy.org/api/interfaces/Community.html"""

    description: str = None
    icon: str = None
    name: str = None
    title: str = None
    removed: bool = None
    published: str = None
    deleted: bool = None
    nsfw: bool = None
    hidden: bool = None
    posting_restricted_to_mods: bool = None
    updated: str = None
    banner: bool = None


@dataclass
class CommunityAggregates(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/CommunityAggregates.html"""

    community_id: int = None
    subscribers: int = None
    posts: int = None
    comments: int = None
    published: str = None
    users_active_day: int = None
    users_active_week: int = None
    users_active_month: int = None
    users_active_half_year: int = None
    hot_rank: int = None


@dataclass
class CustomEmoji(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/CustomEmoji.html"""

    alt_text: str = None
    category: str = None
    image_url: str = None
    local_site_id: int = None
    published: str = None
    shortcode: str = None
    updated: str = None


@dataclass
class CustomEmojiKeyword(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/CustomEmojiKeyword.html"""

    custom_emoji_id: int = None
    keyword: str = None


@dataclass
class ImageFile:
    """https://join-lemmy.org/api/interfaces/ImageFile.html"""

    delete_token: str = None
    file: str = None


@dataclass
class Instance(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/Instance.html"""

    domain: str = None
    published: str = None
    software: str = None
    updated: str = None
    version: str = None


@dataclass
class Language(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/Language.html"""

    code: str = None
    name: str = None


@dataclass
class LocalSite(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/LocalSite.html"""

    actor_name_max_length: int = None
    application_email_admins: bool = None
    application_question: str = None
    captcha_difficulty: str = None
    captcha_enabled: bool = None
    community_creation_admin_only: bool = None
    default_post_listing_type: str = None
    default_theme: str = None
    enable_downvotes: bool = None
    enable_nsfw: bool = None
    federation_enabled: bool = None
    hide_modlog_mod_names: bool = None
    legal_information: str = None
    private_instance: bool = None
    published: str = None
    registration_mode: str = None
    reports_email_admins: bool = None
    require_email_verification: bool = None
    site_id: int = None
    site_setup: bool = None
    slur_filter_regex: str = None
    updated: str = None


@dataclass
class LocalSiteRateLimit(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/LocalSiteRateLimit.html"""

    comment: int = None
    comment_per_second: int = None
    image: int = None
    image_per_second: int = None
    local_site_id: int = None
    message: int = None
    message_per_second: int = None
    post: int = None
    post_per_second: int = None
    published: str = None
    register: int = None
    register_per_second: int = None
    search: int = None
    search_per_second: int = None
    updated: str = None


@dataclass
class LocalUser(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/LocalUser.html"""

    accepted_application: bool = None
    default_listing_type: str = None
    default_sort_type: str = None
    email: str = None
    email_verified: bool = None
    interface_language: str = None
    open_links_in_new_tab: bool = None
    person_id: int = None
    send_notifications_to_email: bool = None
    show_avatars: bool = None
    show_bot_accounts: bool = None
    show_new_post_notifs: bool = None
    show_nsfw: bool = None
    show_read_posts: bool = None
    show_scores: bool = None
    theme: str = None
    totp_2fa_url: str = None
    validator_time: str = None


@dataclass
class ModAdd(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/ModAdd.html"""

    mod_person_id: int = None
    other_person_id: int = None
    removed: bool = None
    when_: str = None


@dataclass
class ModAddCommunity(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/ModAddCommunity.html"""

    community_id: int = None
    mod_person_id: int = None
    other_person_id: int = None
    removed: bool = None
    when_: str = None


@dataclass
class ModBan(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/ModBan.html"""

    banned: bool = None
    expires: str = None
    mod_person_id: int = None
    other_person_id: int = None
    reason: str = None
    when_: str = None


@dataclass
class ModBanFromCommunity(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/ModBanFromCommunity.html"""

    banned: bool = None
    community_id: int = None
    expires: str = None
    mod_person_id: int = None
    other_person_id: int = None
    reason: str = None
    when_: str = None


@dataclass
class ModFeaturePost(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/ModFeaturePost.html"""

    featured: bool = None
    is_featured_community: bool = None
    mod_person_id: int = None
    post_id: int = None
    when_: str = None


@dataclass
class ModHideCommunity(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/ModHideCommunity.html"""

    community_id: int = None
    hidden: bool = None
    mod_person_id: int = None
    reason: str = None
    when_: str = None


@dataclass
class ModLockPost(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/ModLockPost.html"""

    locked: bool = None
    mod_person_id: int = None
    post_id: int = None
    when_: str = None


@dataclass
class ModRemoveComment(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/ModRemoveComment.html"""

    comment_id: int = None
    mod_person_id: int = None
    removed: bool = None
    reason: str = None
    when_: str = None


@dataclass
class ModRemoveCommunity(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/ModRemoveCommunity.html"""

    community_id: int = None
    expires: str = None
    mod_person_id: int = None
    removed: bool = None
    reason: str = None
    when_: str = None


@dataclass
class ModRemovePost(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/ModRemovePost.html"""

    mod_person_id: int = None
    post_id: int = None
    removed: bool = None
    reason: str = None
    when_: str = None


@dataclass
class ModTransferCommunity(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/ModTransferCommunity.html"""

    community_id: int = None
    mod_person_id: int = None
    other_person_id: int = None
    when_: str = None


@dataclass
class Person(_InstanceBound):
    """https://join-lemmy.org/api/interfaces/Person.html"""

    admin: bool = None
    avatar: str = None
    ban_expires: str = None
    banned: bool = None
    banner: str = None
    bio: str = None
    bot_account: bool = None
    deleted: bool = None
    display_name: str = None
    inbox_url: str = None
    matrix_user_id: str = None
    name: str = None
    published: str = None
    updated: str = None


@dataclass
class PersonAggregates(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/PersonAggregates.html"""

    comment_count: int = None
    comment_score: int = None
    person_id: int = None
    post_count: int = None
    post_score: int = None


@dataclass
class PersonMention(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/PersonMention.html"""

    comment_id: int = None
    published: str = None
    read: bool = None
    recipient_id: int = None


@dataclass
class Post(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/Post.html"""

    ap_id: str = None
    body: str = None
    community_id: int = None
    creator_id: int = None
    deleted: bool = None
    embed_description: str = None
    embed_title: str = None
    embed_video_url: str = None
    featured_community: bool = None
    featured_local: bool = None
    language_id: int = None
    local: bool = None
    locked: bool = None
    name: str = None
    nsfw: bool = None
    published: str = None
    removed: bool = None
    thumbnail_url: str = None
    updated: str = None
    url: str = None


@dataclass
class PostAggregates(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/PostAggregates.html"""

    comments: int = None
    downvotes: int = None
    featured_community: bool = None
    featured_local: bool = None
    hot_rank: int = None
    hot_rank_active: int = None
    newest_comment_time: str = None
    newest_comment_time_necro: str = None
    post_id: int = None
    published: str = None
    score: int = None
    upvotes: int = None


@dataclass
class PostReport(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/PostReport.html"""

    creator_id: int = None
    original_post_body: str = None
    original_post_name: str = None
    original_post_url: str = None
    post_id: int = None
    published: str = None
    reason: str = None
    resolved: bool = None
    resolver_id: int = None
    updated: str = None


@dataclass
class PrivateMessage(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/PrivateMessage.html"""

    ap_id: str = None
    content: str = None
    creator_id: int = None
    deleted: bool = None
    local: bool = None
    published: str = None
    read: bool = None
    recipient_id: int = None
    updated: str = None


@dataclass
class PrivateMessageReport(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/PrivateMessageReport.html"""

    creator_id: int = None
    original_pm_text: str = None
    private_message_id: int = None
    published: str = None
    reason: str = None
    resolved: bool = None
    resolver_id: int = None
    updated: str = None


@dataclass
class RegistrationApplication(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/RegistrationApplication.html"""

    admin_id: int = None
    answer: str = None
    deny_reason: str = None
    local_user_id: int = None
    published: str = None


@dataclass
class Site(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/Site.html"""

    actor_id: str = None
    banner: str = None
    description: str = None
    icon: str = None
    inbox_url: str = None
    instance_id: int = None
    last_refreshed_at: str = None
    name: str = None
    private_key: str = None
    public_key: str = None
    published: str = None
    sidebar: str = None
    updated: str = None


@dataclass
class SiteAggregates(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/SiteAggregates.html"""

    comments: int = None
    communities: int = None
    posts: int = None
    site_id: int = None
    users: int = None
    users_active_day: int = None
    users_active_half_year: int = None
    users_active_month: int = None
    users_active_week: int = None


@dataclass
class SiteMetadata:
    """https://join-lemmy.org/api/interfaces/SiteMetadata.html"""

    description: str = None
    embed_video_url: str = None
    image: str = None
    title: str = None


@dataclass
class Tagline(_LemmyObject):
    """https://join-lemmy.org/api/interfaces/Tagline.html"""

    content: str = None
    local_site_id: int = None
    published: str = None
    updated: str = None
