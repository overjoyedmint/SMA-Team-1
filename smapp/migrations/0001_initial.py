# Generated by Django 3.2.4 on 2021-06-25 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_type', models.CharField(max_length=255)),
                ('updated_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_email_verified', models.BooleanField()),
                ('status', models.CharField(max_length=255)),
                ('password', models.CharField(default='user', max_length=255)),
                ('bio', models.CharField(max_length=255)),
                ('occupation', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('followers_count', models.IntegerField(default=0)),
                ('following_count', models.IntegerField(default=0)),
                ('profile_picture', models.ImageField(upload_to='')),
                ('updated_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User_Socials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_link', models.CharField(max_length=255)),
                ('github_link', models.CharField(max_length=255)),
                ('linkedin_link', models.CharField(max_length=255)),
                ('instagram_link', models.CharField(max_length=255)),
                ('twitter_link', models.CharField(max_length=255)),
                ('updated_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='smapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='User_Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_post_notification_subscribed', models.BooleanField()),
                ('status', models.BooleanField()),
                ('updated_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='smapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('likes_count', models.IntegerField(default=0)),
                ('comments_count', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='smapp.categories')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='smapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='Post_Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='smapp.posts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='smapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='Post_Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('updated_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='smapp.posts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='smapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='Password_Resets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
                ('is_token_used', models.BooleanField()),
                ('expired_at', models.DateTimeField(default=None)),
                ('updated_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='smapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('read_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='smapp.users')),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='smapp.users'),
        ),
    ]
