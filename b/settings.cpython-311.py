�
    ϥf:  �                   �  � d Z ddlmZ ddlmZ  e�   �         Ze�                    �   �           ee�  �        �                    �   �         j	        j	        Z
e�                    d�  �        ZdZdgZg d�Zg d�Zd	Zd
 ee
�                    d�  �        �  �        gddg d�id�gZdZde�                    d�  �        iZddiddiddiddigZdZdZdZdZdZ ee
�                    d�  �        �  �        gZ ee
�                    d�  �        �  �        ZdZdZ dZ!d Z"d Z#d!Z$d!Z%d"Z&d#Z' ee
�                    d$�  �        �  �        Z(d%S )&a&  
Django settings for b project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
�    )�Path)�Env�
SECRET_KEYFz	127.0.0.1)zdjango.contrib.adminzdjango.contrib.authzdjango.contrib.contenttypeszdjango.contrib.sessionszdjango.contrib.messageszwhitenoise.runserver_nostaticzdjango.contrib.staticfiles�crispy_forms�crispy_bootstrap5�accounts�pages�articles)z-django.middleware.security.SecurityMiddlewarez4django.contrib.sessions.middleware.SessionMiddlewarez*whitenoise.middleware.WhiteNoiseMiddlewarez)django.middleware.common.CommonMiddlewarez)django.middleware.csrf.CsrfViewMiddlewarez7django.contrib.auth.middleware.AuthenticationMiddlewarez4django.contrib.messages.middleware.MessageMiddlewarez6django.middleware.clickjacking.XFrameOptionsMiddlewarezb.urlsz/django.template.backends.django.DjangoTemplates�templateT�context_processors)z(django.template.context_processors.debugz*django.template.context_processors.requestz+django.contrib.auth.context_processors.authz3django.contrib.messages.context_processors.messages)�BACKEND�DIRS�APP_DIRS�OPTIONSzb.wsgi.application�default�DATABASE_URL�NAMEzHdjango.contrib.auth.password_validation.UserAttributeSimilarityValidatorz>django.contrib.auth.password_validation.MinimumLengthValidatorz?django.contrib.auth.password_validation.CommonPasswordValidatorz@django.contrib.auth.password_validation.NumericPasswordValidator�uzzAsia/Tashkentz/static/�static�staticfilesz7whitenoise.storage.CompressedManifestStaticFilesStoragezdjango.db.models.BigAutoFieldzaccounts.CustomUser�home�
bootstrap5z.django.core.mail.backends.console.EmailBackendz/media/�mediaN))�__doc__�pathlibr   �environsr   �env�read_env�__file__�resolve�parent�BASE_DIR�strr   �DEBUG�ALLOWED_HOSTS�INSTALLED_APPS�
MIDDLEWARE�ROOT_URLCONF�joinpath�	TEMPLATES�WSGI_APPLICATION�	dj_db_url�	DATABASES�AUTH_PASSWORD_VALIDATORS�LANGUAGE_CODE�	TIME_ZONE�USE_I18N�USE_TZ�
STATIC_URL�STATICFILES_DIRS�STATIC_ROOT�STATICFILES_STORAGE�DEFAULT_AUTO_FIELD�AUTH_USER_MODEL�LOGIN_REDIRECT_URL�LOGOUT_REDIRECT_URL�CRISPY_ALLOWED_TEMPLATE_PACKS�CRISPY_TEMPLATE_PACK�EMAIL_BACKEND�	MEDIA_URL�
MEDIA_ROOT� �    �#/storage/emulated/0/a/b/settings.py�<module>rC      s  ��
� 
� � � � � � � � � � � � ��C�E�E�� ������ �4��>�>�!�!�#�#�*�1�� �W�W�\�"�"�
� �����
� � ��	� 	� 	�
� �� E���X�&�&�z�2�2�3�3�4�� � #� #� #�
�	� ��	�  (� � �s�}�}�^�,�,��	� 	�Z�� 	�P�� 	�Q�� 	�R��� �& ���	���	�� �
��C��)�)�(�3�3�4�4�5� ��c�(�#�#�M�2�2�3�3��O� �
 5� � (�� � �� � ,� �#� �@�� �	��S��"�"�7�+�+�,�,�
�
�
rA   