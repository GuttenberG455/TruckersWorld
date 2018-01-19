from django.forms import *
from django.contrib.auth import *
from social.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

Choices_Gender = ((0, 'Не указывать'), ('М', 'М'), ('Ж', 'Ж'))
Choices_Group = ((1, 'Пользователь'), (2, 'Компания'), (3, 'Модератор'))
Years = {2018: '2018', 2017: '2017', 2016: '2016', 2015: '2015', 2014: '2014', 2013: '2013', 2012: '2012',
         2011: '2011',
         2010: '2010', 2009: '2009', 2008: '2008', 2007: '2007', 2006: '2006', 2005: '2005', 2004: '2004', 2003: '2003',
         2002: '2002', 2001: '2001', 2000: '2000', 1999: '1999', 1998: '1998', 1997: '1997', 1996: '1996', 1995: '1995',
         1994: '1994', 1993: '1993', 1992: '1992', 1991: '1991', 1990: '1990', 1989: '1989', 1988: '1988', 1987: '1987',
         1986: '1986', 1985: '1985', 1984: '1984', 1983: '1983', 1982: '1982', 1981: '1981', 1980: '1980', 1979: '1979',
         1978: '1978', 1977: '1977', 1976: '1976', 1975: '1975', 1974: '1974', 1973: '1973', 1972: '1972', 1971: '1971',
         1970: '1970', 1969: '1969', 1968: '1968', 1967: '1967', 1966: '1966', 1965: '1965', 1964: '1964', 1963: '1963',
         1962: '1962', 1961: '1961', 1960: '1960', 1959: '1959', 1958: '1958', 1957: '1957', 1956: '1956', 1955: '1955',
         1954: '1954', 1953: '1953', 1952: '1952', 1951: '1951', 1950: '1950', 1949: '1949', 1948: '1948', 1947: '1947',
         1946: '1946', 1945: '1945', 1944: '1944', 1943: '1943', 1942: '1942', 1941: '1941', 1940: '1940', 1939: '1939',
         1938: '1938', 1937: '1937', 1936: '1936', 1935: '1935', 1934: '1934', 1933: '1933', 1932: '1932', 1931: '1931',
         1930: '1930', 1929: '1929', 1928: '1928', 1927: '1927', 1926: '1926', 1925: '1925', 1924: '1924', 1923: '1923',
         1922: '1922', 1921: '1921', 1920: '1920'}


class AuthorizationForm(Form):
    username = CharField(label='username', max_length=100)
    password = CharField(label='password', widget=PasswordInput)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title_post", "text_post", "image1_post", "image2_post", "image3_post", "image4_post", "image5_post",
                  "author_post"]


class RegistrationForm(UserCreationForm):
    form_gender = ChoiceField(widget=Select, choices=Choices_Gender)
    form_group = ChoiceField(widget=Select, choices=Choices_Group)
    form_date_of_birth = DateField(widget=SelectDateWidget(years=Years, empty_label=('День', 'Месяц', 'Год')),
                                   required=False)
    form_phone = CharField(max_length=15, required=False)
    form_company_name = CharField(max_length=127, required=False)
    form_mod_code = CharField(max_length=6, required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        group_pers = self.cleaned_data['form_group']
        gender_pers = self.cleaned_data['form_gender']
        date_of_birth_pers = self.cleaned_data['form_date_of_birth']
        phone_pers = self.cleaned_data['form_phone']
        company_pers = self.cleaned_data['form_company_name']
        mod_code = self.cleaned_data['form_mod_code']
        if commit:
            if group_pers == 3:
                if mod_code == "REACT":
                    user.save()
                    user_personal = UserPersonal(user_django_id=user.id, user_group_id_id=group_pers,
                                                 user_name=user.first_name,
                                                 user_surname=user.last_name)
                    # user_phone_number=phone_pers,
                    # user_company_name=company_pers)
                    user_personal.save()
            else:
                print("OKAY?")
            user.save()
            user_personal = UserPersonal(user_django_id=user.id, user_group_id_id=group_pers,
                                         user_name=user.first_name,
                                         user_surname=user.last_name,
                                         user_phone_number=phone_pers,
                                         user_company_name=company_pers,
                                         user_gender=gender_pers,
                                         user_dateofbirth=date_of_birth_pers)
            user_personal.save()
        return user


class CommentForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ('commentary_text', 'commentary_author', 'commentary_link', 'commentary_date')


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ["video_link", "video_name", "video_description", "video_author"]


class EditPersonalForm(ModelForm):
    class Meta:
        model = UserPersonal
        fields = ('user_name', 'user_surname', 'user_gender', 'user_dateofbirth', 'user_company_name', 'user_image',
                  'user_phone_number')


class TruckForm(ModelForm):
    class Meta:
        model = Truck
        fields = ('truck_brend', 'truck_model', 'truck_release_year', 'truck_type', 'truck_mileage', 'truck_gosnum',
                  'truck_vinnum', 'truck_engine', 'truck_engine_vol', 'truck_engine_power', 'truck_wheel_formula',
                  'truck_image', 'truck_owner')
