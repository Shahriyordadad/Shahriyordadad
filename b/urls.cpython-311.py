�
    ��f�  �                   �z  � d Z ddlmZ ddlmZmZ ddlmZ ddlm	Z	  ed ed�  �        �  �         edej
        j        �  �         ed	 ed
�  �        �  �         ed	 ed�  �        �  �         ed ed�  �        �  �         ed ed�  �        �  �        gZej        re e	ej        ej        ��  �        z  ZdS dS )ax  
URL configuration for b project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
�    )�admin)�path�include)�settings)�staticz	ckeditor/zckeditor_uploader.urlszadmin/z	accounts/zaccounts.urlszdjango.contrib.auth.urlsz	articles/zarticles.urls� z
pages.urls)�document_rootN)�__doc__�django.contribr   �django.urlsr   r   �django.confr   �django.conf.urls.staticr   �site�urls�urlpatterns�DEBUG�	MEDIA_URL�
MEDIA_ROOT� �    �/storage/emulated/0/a/b/urls.py�<module>r      s6  ��� �  !�  �  �  �  �  � %� %� %� %� %� %� %� %�  �  �  �  �  �  � *� *� *� *� *� *� 	�D��g�g�6�7�7�8�8��D��5�:�?�#�#��$�{�G�G�O�,�,�-�-��$�{�G�G�6�7�7�8�8��$�{�G�G�O�,�,�-�-��$�r�7�7�<� � �!�!��� �>� P��6�6�(�,�8�;N�O�O�O�O�K�K�K�P� Pr   