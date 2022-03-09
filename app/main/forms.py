from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    post = TextAreaField('Pitch', validators=[InputRequired()])
    category = SelectField('Category', choices=[('PRODUCT', 'PRODUCT'), ('IDEA', 'IDEA'), ('Business', 'Business')],
                           validators=[InputRequired()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[InputRequired()])
    submit = SubmitField('Post')


class Vote(FlaskForm):
    submit = SelectField('Like')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('bio', validators=[InputRequired()])
    submit = SubmitField('Post')