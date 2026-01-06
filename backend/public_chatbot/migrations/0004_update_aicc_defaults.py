# Generated manually to update defaults
from django.db import migrations, models


def update_existing_config(apps, schema_editor):
    """Update existing ChatbotConfiguration with new defaults"""
    ChatbotConfiguration = apps.get_model('public_chatbot', 'ChatbotConfiguration')
    
    # Get existing config or create with new defaults
    try:
        config = ChatbotConfiguration.objects.get(pk=1)
        # Update existing config with new defaults
        config.default_model = 'gpt-4.1-2025-04-14'
        config.similarity_threshold = 0.05
        config.system_prompt = """You are a professional website assistant. Your purpose is to provide clear, accurate, and professional responses to queries, directing users to relevant resources when appropriate.

[CORE RULES]

Keep answers short: maximum 4–6 sentences.
Always use a clear, professional, and actionable tone.
Only use facts explicitly provided to you or that are certain; never speculate or invent.
Never fabricate information, URLs, or guarantees you cannot fulfil.
When unsure or if information is missing, respond by politely asking the user for clarification or directing them to official sources.

[USAGE GUIDELINES]

Reference the most relevant URL(s) based on the user's query
For complex questions spanning multiple areas, direct users to the main contact page or most relevant starting point
Always provide the specific URL rather than saying "visit our website\""""
        config.save()
        print(f"✅ Updated existing ChatbotConfiguration with new defaults")
    except ChatbotConfiguration.DoesNotExist:
        # No existing config, the get_config() method will create one with new defaults
        print("ℹ️ No existing config found - new defaults will be applied on first use")


def reverse_update_config(apps, schema_editor):
    """Reverse migration - restore previous defaults"""
    ChatbotConfiguration = apps.get_model('public_chatbot', 'ChatbotConfiguration')
    
    try:
        config = ChatbotConfiguration.objects.get(pk=1)
        # Restore previous defaults
        config.default_model = 'gpt-3.5-turbo'
        config.similarity_threshold = 0.7
        config.system_prompt = "You are a helpful assistant providing accurate, concise responses."
        config.save()
        print("↩️ Restored previous ChatbotConfiguration defaults")
    except ChatbotConfiguration.DoesNotExist:
        print("ℹ️ No existing config to reverse")


class Migration(migrations.Migration):
    
    dependencies = [
        ('public_chatbot', '0003_add_vector_search_toggle'),
    ]
    
    operations = [
        # Update model field defaults
        migrations.AlterField(
            model_name='chatbotconfiguration',
            name='default_model',
            field=models.CharField(default='gpt-4.1-2025-04-14', max_length=100),
        ),
        migrations.AlterField(
            model_name='chatbotconfiguration',
            name='similarity_threshold',
            field=models.FloatField(default=0.05),
        ),
        migrations.AlterField(
            model_name='chatbotconfiguration',
            name='system_prompt',
            field=models.TextField(
                default="""You are a professional website assistant. Your purpose is to provide clear, accurate, and professional responses to queries, directing users to relevant resources when appropriate.

[CORE RULES]

Keep answers short: maximum 4–6 sentences.
Always use a clear, professional, and actionable tone.
Only use facts explicitly provided to you or that are certain; never speculate or invent.
Never fabricate information, URLs, or guarantees you cannot fulfil.
When unsure or if information is missing, respond by politely asking the user for clarification or directing them to official sources.

[USAGE GUIDELINES]

Reference the most relevant URL(s) based on the user's query
For complex questions spanning multiple areas, direct users to the main contact page or most relevant starting point
Always provide the specific URL rather than saying "visit our website\"""",
                help_text="System prompt that defines the AI assistant's behavior and personality"
            ),
        ),
        # Data migration to update existing configuration
        migrations.RunPython(update_existing_config, reverse_update_config),
    ]