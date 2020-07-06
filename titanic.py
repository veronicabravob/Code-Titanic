{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Análisis exploratorio de datos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "dftrain = pd.read_csv(\"train.csv\")\n",
    "dftest = pd.read_csv(\"test.csv\")\n",
    "dfgendersubmission = pd.read_csv(\"gender_submission.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(891, 12)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftrain.shape #Dimensión de la base de datos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 891 entries, 0 to 890\n",
      "Data columns (total 12 columns):\n",
      " #   Column       Non-Null Count  Dtype  \n",
      "---  ------       --------------  -----  \n",
      " 0   PassengerId  891 non-null    int64  \n",
      " 1   Survived     891 non-null    int64  \n",
      " 2   Pclass       891 non-null    int64  \n",
      " 3   Name         891 non-null    object \n",
      " 4   Sex          891 non-null    object \n",
      " 5   Age          714 non-null    float64\n",
      " 6   SibSp        891 non-null    int64  \n",
      " 7   Parch        891 non-null    int64  \n",
      " 8   Ticket       891 non-null    object \n",
      " 9   Fare         891 non-null    float64\n",
      " 10  Cabin        204 non-null    object \n",
      " 11  Embarked     889 non-null    object \n",
      "dtypes: float64(2), int64(5), object(5)\n",
      "memory usage: 83.7+ KB\n"
     ]
    }
   ],
   "source": [
    "dftrain.info() #Información sobre las variables del dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                           Allen, Mr. William Henry    male  35.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Cabin Embarked  \n",
       "0      0         A/5 21171   7.2500   NaN        S  \n",
       "1      0          PC 17599  71.2833   C85        C  \n",
       "2      0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3      0            113803  53.1000  C123        S  \n",
       "4      0            373450   8.0500   NaN        S  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftrain.head() #Encabezado del dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#pd.set_option('display.max_rows', dftrain.shape[0]+1) #Base de datos entera\n",
    "#dftrain"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId      0\n",
       "Survived         0\n",
       "Pclass           0\n",
       "Name             0\n",
       "Sex              0\n",
       "Age            177\n",
       "SibSp            0\n",
       "Parch            0\n",
       "Ticket           0\n",
       "Fare             0\n",
       "Cabin          687\n",
       "Embarked         2\n",
       "dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftrain.isnull().sum() #Variables con datos nulos"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "En la base de datos analizamos los diferentes tipos de variables, algunas serán descartadas ya que se considera que no son relevantes dentro del modelo\n",
    "\n",
    "Las variables que serán descartadas son:\n",
    "\n",
    "Name\n",
    "Ticket\n",
    "Fare\n",
    "Embarked\n",
    "Las otras variables se consideran relevantes para el modelo,\n",
    "\n",
    "Survived: Es la variable dependiente del modelo\n",
    "\n",
    "Pclass: Esta variable nos muestra en la clase que viajaban los pasajeros en el barco, puede ser explicativa ya que se supone que le dan prioridad a las primeras clases\n",
    "\n",
    "Sex: Esta variable nos muestra el sexo de los pasajeros, puede ser explicartiva ya que se supone que le dan prioridad a las mujeres\n",
    "\n",
    "Age: Es la variable con la edad de los pasajeros, puede ser explicativa ya que se supone que le dan prioridad a las personas más jovenes\n",
    "\n",
    "SibSp: Es la variable que nos muestra el número de herman@s que tiene el pasajero, puede ser explicativa ya que se supone que le dan prioridad a aquel que viaje con sus herman@s\n",
    "\n",
    "Parch: Es la variable que nos muestra el número de hijos que tiene el pasajero, puede ser explicativa ya que se supone que le dan prioridad a personas que tengan hijos para que estos no queden huérfanos\n",
    "\n",
    "cabin: Es la variable que nos muestra en que cabina estaba ubicado el pasajero, puede ser explicativa ya que se supone que es mas probable que las personas que estuvieran más cerca de la borda del barco les tocara puesto en los botes salvavidas, y así tener mas tiempo para salvarse."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Cabin</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>C85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>C123</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>887</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>male</td>\n",
       "      <td>27.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>888</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>19.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>B42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>889</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>female</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>890</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>male</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>C148</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>891</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>male</td>\n",
       "      <td>32.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass     Sex   Age  SibSp  Parch Cabin\n",
       "0              1         0       3    male  22.0      1      0   NaN\n",
       "1              2         1       1  female  38.0      1      0   C85\n",
       "2              3         1       3  female  26.0      0      0   NaN\n",
       "3              4         1       1  female  35.0      1      0  C123\n",
       "4              5         0       3    male  35.0      0      0   NaN\n",
       "..           ...       ...     ...     ...   ...    ...    ...   ...\n",
       "886          887         0       2    male  27.0      0      0   NaN\n",
       "887          888         1       1  female  19.0      0      0   B42\n",
       "888          889         0       3  female   NaN      1      2   NaN\n",
       "889          890         1       1    male  26.0      0      0  C148\n",
       "890          891         0       3    male  32.0      0      0   NaN\n",
       "\n",
       "[891 rows x 8 columns]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftrain = dftrain.drop([\"Name\",\"Ticket\",\"Fare\",\"Embarked\"],axis=1) # Descartamos las variables que no son de interés\n",
    "dftrain"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Cabin</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>C85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>C123</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>887</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>male</td>\n",
       "      <td>27.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>888</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>19.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>B42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>889</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>female</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>890</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>male</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>C148</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>891</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>male</td>\n",
       "      <td>32.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass     Sex   Age  SibSp  Parch Cabin\n",
       "0              1         0       3    male  22.0      1      0     0\n",
       "1              2         1       1  female  38.0      1      0   C85\n",
       "2              3         1       3  female  26.0      0      0     0\n",
       "3              4         1       1  female  35.0      1      0  C123\n",
       "4              5         0       3    male  35.0      0      0     0\n",
       "..           ...       ...     ...     ...   ...    ...    ...   ...\n",
       "886          887         0       2    male  27.0      0      0     0\n",
       "887          888         1       1  female  19.0      0      0   B42\n",
       "888          889         0       3  female   0.0      1      2     0\n",
       "889          890         1       1    male  26.0      0      0  C148\n",
       "890          891         0       3    male  32.0      0      0     0\n",
       "\n",
       "[891 rows x 8 columns]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftrain = dftrain.fillna(0) #Reemplazamos los datos nulos por 0s\n",
    "dftrain"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId    0\n",
       "Survived       0\n",
       "Pclass         0\n",
       "Sex            0\n",
       "Age            0\n",
       "SibSp          0\n",
       "Parch          0\n",
       "Cabin          0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftrain.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Cabin</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PassengerId</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>C85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>C123</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>male</td>\n",
       "      <td>27.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>19.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>B42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>female</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>male</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>C148</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>891</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>male</td>\n",
       "      <td>32.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             Survived  Pclass     Sex   Age  SibSp  Parch Cabin\n",
       "PassengerId                                                    \n",
       "1                   0       3    male  22.0      1      0     0\n",
       "2                   1       1  female  38.0      1      0   C85\n",
       "3                   1       3  female  26.0      0      0     0\n",
       "4                   1       1  female  35.0      1      0  C123\n",
       "5                   0       3    male  35.0      0      0     0\n",
       "...               ...     ...     ...   ...    ...    ...   ...\n",
       "887                 0       2    male  27.0      0      0     0\n",
       "888                 1       1  female  19.0      0      0   B42\n",
       "889                 0       3  female   0.0      1      2     0\n",
       "890                 1       1    male  26.0      0      0  C148\n",
       "891                 0       3    male  32.0      0      0     0\n",
       "\n",
       "[891 rows x 7 columns]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftrain = dftrain.set_index(\"PassengerId\") #Cambiamos el indice por passanger Id\n",
    "dftrain"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "148"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "matriz= dftrain['Cabin'].unique() #Valores unicos de la variable Cabin\n",
    "len(matriz) #Cantidad de valores únicos de la variable Cabin"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 'C85' 'C123' 'E46' 'G6' 'C103' 'D56' 'A6' 'C23 C25 C27' 'B78' 'D33'\n",
      " 'B30' 'C52' 'B28' 'C83' 'F33' 'F G73' 'E31' 'A5' 'D10 D12' 'D26' 'C110'\n",
      " 'B58 B60' 'E101' 'F E69' 'D47' 'B86' 'F2' 'C2' 'E33' 'B19' 'A7' 'C49'\n",
      " 'F4' 'A32' 'B4' 'B80' 'A31' 'D36' 'D15' 'C93' 'C78' 'D35' 'C87' 'B77'\n",
      " 'E67' 'B94' 'C125' 'C99' 'C118' 'D7' 'A19' 'B49' 'D' 'C22 C26' 'C106'\n",
      " 'C65' 'E36' 'C54' 'B57 B59 B63 B66' 'C7' 'E34' 'C32' 'B18' 'C124' 'C91'\n",
      " 'E40' 'T' 'C128' 'D37' 'B35' 'E50' 'C82' 'B96 B98' 'E10' 'E44' 'A34'\n",
      " 'C104' 'C111' 'C92' 'E38' 'D21' 'E12' 'E63' 'A14' 'B37' 'C30' 'D20' 'B79'\n",
      " 'E25' 'D46' 'B73' 'C95' 'B38' 'B39' 'B22' 'C86' 'C70' 'A16' 'C101' 'C68'\n",
      " 'A10' 'E68' 'B41' 'A20' 'D19' 'D50' 'D9' 'A23' 'B50' 'A26' 'D48' 'E58'\n",
      " 'C126' 'B71' 'B51 B53 B55' 'D49' 'B5' 'B20' 'F G63' 'C62 C64' 'E24' 'C90'\n",
      " 'C45' 'E8' 'B101' 'D45' 'C46' 'D30' 'E121' 'D11' 'E77' 'F38' 'B3' 'D6'\n",
      " 'B82 B84' 'D17' 'A36' 'B102' 'B69' 'E49' 'C47' 'D28' 'E17' 'A24' 'C50'\n",
      " 'B42' 'C148']\n"
     ]
    }
   ],
   "source": [
    "print(matriz)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "matriz2= dftrain['Sex'].unique()\n",
    "len(matriz2) #Cantidad de valores únicos de la variable Cabin"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Se comprueba que en las variables está el total de los individuos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "male      577\n",
       "female    314\n",
       "Name: Sex, dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftrain['Sex'].value_counts() #Cantidad de hombres/mujeres que habían en el titanic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "% of women who survived: 0.7420382165605095\n"
     ]
    }
   ],
   "source": [
    "women = dftrain.loc[dftrain.Sex == \"female\"][\"Survived\"]\n",
    "rate_women = sum(women)/len(women)\n",
    "print(\"% of women who survived:\", rate_women)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "% of male who survived: 0.18890814558058924\n"
     ]
    }
   ],
   "source": [
    "male = dftrain.loc[dftrain.Sex == \"male\"][\"Survived\"]\n",
    "rate_male = sum(male)/len(male)\n",
    "print(\"% of male who survived:\", rate_male)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3    491\n",
       "1    216\n",
       "2    184\n",
       "Name: Pclass, dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftrain['Pclass'].value_counts() #Cantidad de personas que habían por clase en el titanic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "% of first class peoples who survived 0.6296296296296297\n",
      "% of second class peoples who survived 0.47282608695652173\n",
      "% of third class peoples who survived 0.24236252545824846\n"
     ]
    }
   ],
   "source": [
    "firstclass = dftrain.loc[dftrain.Pclass == 1][\"Survived\"]\n",
    "rate_firstclass = sum(firstclass)/len(firstclass)\n",
    "print(\"% of first class peoples who survived\", rate_firstclass)\n",
    "\n",
    "secondclass = dftrain.loc[dftrain.Pclass == 2][\"Survived\"]\n",
    "rate_secondclass = sum(secondclass)/len(secondclass)\n",
    "print(\"% of second class peoples who survived\", rate_secondclass)\n",
    "\n",
    "thirdclass = dftrain.loc[dftrain.Pclass == 3][\"Survived\"]\n",
    "rate_thirdclass = sum(thirdclass)/len(thirdclass)\n",
    "print(\"% of third class peoples who survived\", rate_thirdclass)\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>0.383838</td>\n",
       "      <td>2.308642</td>\n",
       "      <td>23.799293</td>\n",
       "      <td>0.523008</td>\n",
       "      <td>0.381594</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.486592</td>\n",
       "      <td>0.836071</td>\n",
       "      <td>17.596074</td>\n",
       "      <td>1.102743</td>\n",
       "      <td>0.806057</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>6.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Survived      Pclass         Age       SibSp       Parch\n",
       "count  891.000000  891.000000  891.000000  891.000000  891.000000\n",
       "mean     0.383838    2.308642   23.799293    0.523008    0.381594\n",
       "std      0.486592    0.836071   17.596074    1.102743    0.806057\n",
       "min      0.000000    1.000000    0.000000    0.000000    0.000000\n",
       "25%      0.000000    2.000000    6.000000    0.000000    0.000000\n",
       "50%      0.000000    3.000000   24.000000    0.000000    0.000000\n",
       "75%      1.000000    3.000000   35.000000    1.000000    0.000000\n",
       "max      1.000000    3.000000   80.000000    8.000000    6.000000"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftrain.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Cabin</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PassengerId</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>C85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>C123</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>27.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>19.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>B42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>C148</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>891</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>32.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             Survived  Pclass  Sex   Age  SibSp  Parch Cabin\n",
       "PassengerId                                                 \n",
       "1                   0       3    1  22.0      1      0     0\n",
       "2                   1       1    0  38.0      1      0   C85\n",
       "3                   1       3    0  26.0      0      0     0\n",
       "4                   1       1    0  35.0      1      0  C123\n",
       "5                   0       3    1  35.0      0      0     0\n",
       "...               ...     ...  ...   ...    ...    ...   ...\n",
       "887                 0       2    1  27.0      0      0     0\n",
       "888                 1       1    0  19.0      0      0   B42\n",
       "889                 0       3    0   0.0      1      2     0\n",
       "890                 1       1    1  26.0      0      0  C148\n",
       "891                 0       3    1  32.0      0      0     0\n",
       "\n",
       "[891 rows x 7 columns]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftrain['Sex'].replace(['female','male'],[0,1],inplace=True) #Nos cambia la variable female por 0 y male por 1\n",
    "dftrain"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Cantidad de mujeres y hombres en el train "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Grafico del género de los donantes\n",
    "dftrain.groupby('Sex').size().plot(kind='bar')\n",
    "plt.title('Distribución por género train ')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El procentaje de sobrevivientes de la base de datos es 38.38%\n"
     ]
    }
   ],
   "source": [
    "porcent_sobrevivientes = (dftrain[dftrain.Survived\n",
    "                             > 0]['Survived'].count() * 1.0\n",
    "       / dftrain['Survived'].count()) * 100.0\n",
    "print(\"El porcentaje de sobrevivientes de la base de datos es {0:.2f}%\"\n",
    "      .format(porcent_sobrevivientes))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creando subset con solo con los sobrevivientes\n",
    "dftrain_sobrevivientes = dftrain[dftrain.Survived > 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Cabin</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PassengerId</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>C85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>C123</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>27.0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>14.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>876</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>15.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>880</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>56.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>C50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>881</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>25.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>19.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>B42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>C148</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>342 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             Survived  Pclass  Sex   Age  SibSp  Parch Cabin\n",
       "PassengerId                                                 \n",
       "2                   1       1    0  38.0      1      0   C85\n",
       "3                   1       3    0  26.0      0      0     0\n",
       "4                   1       1    0  35.0      1      0  C123\n",
       "9                   1       3    0  27.0      0      2     0\n",
       "10                  1       2    0  14.0      1      0     0\n",
       "...               ...     ...  ...   ...    ...    ...   ...\n",
       "876                 1       3    0  15.0      0      0     0\n",
       "880                 1       1    0  56.0      0      1   C50\n",
       "881                 1       2    0  25.0      0      1     0\n",
       "888                 1       1    0  19.0      0      0   B42\n",
       "890                 1       1    1  26.0      0      0  C148\n",
       "\n",
       "[342 rows x 7 columns]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftrain_sobrevivientes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "342"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(dftrain_sobrevivientes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "dftrain_sobrevivientes.groupby('Sex').size().plot(kind='bar')\n",
    "plt.title('Distribución por género')\n",
    "plt.show()  #Male=1 Female=0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# edad segun el género\n",
    "dftrain_sobrevivientes[(dftrain_sobrevivientes.Age <= 100)\n",
    "             & (dftrain_sobrevivientes.Sex.isin(['0', '1'])\n",
    "               )][['Age', 'Sex']].boxplot(by='Sex')\n",
    "plt.title('edad segun el género')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Age    24.390558\n",
       "dtype: float64"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Media de edad por mujeres \n",
    "dftrain_sobrevivientes[dftrain_sobrevivientes.Sex == 0][['Age']].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pclass    1.950292\n",
       "dtype: float64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Media de clase de sobrevivientes \n",
    "dftrain_sobrevivientes[['Pclass']].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Age    23.272202\n",
       "dtype: float64"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Media de edad por hombres\n",
    "dftrain_sobrevivientes[dftrain_sobrevivientes.Sex == 1][['Age']].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "dftrain_sobrevivientes.groupby('Pclass').size().plot(kind='bar')\n",
    "plt.title('Distribución por clase')\n",
    "plt.show() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>count</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Pclass</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>136</td>\n",
       "      <td>122</td>\n",
       "      <td>7111.42</td>\n",
       "      <td>90</td>\n",
       "      <td>77</td>\n",
       "      <td>216</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>87</td>\n",
       "      <td>108</td>\n",
       "      <td>5168.83</td>\n",
       "      <td>74</td>\n",
       "      <td>70</td>\n",
       "      <td>184</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>119</td>\n",
       "      <td>347</td>\n",
       "      <td>8924.92</td>\n",
       "      <td>302</td>\n",
       "      <td>193</td>\n",
       "      <td>491</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Survived  Sex      Age  SibSp  Parch  count\n",
       "Pclass                                             \n",
       "1            136  122  7111.42     90     77    216\n",
       "2             87  108  5168.83     74     70    184\n",
       "3            119  347  8924.92    302    193    491"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pclass_gender_survival_count_df= dftrain.groupby(['Pclass','Sex'])['Survived'].sum()\n",
    "dftrain.groupby(['Pclass','Sex']).count()\n",
    "dftrain['count'] = 1 # agregar columna\n",
    "dftrain.groupby(['Pclass','Sex','count']).count()\n",
    "dftrain.groupby(['Pclass']).sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pclass  Sex\n",
       "1       0      91\n",
       "        1      45\n",
       "2       0      70\n",
       "        1      17\n",
       "3       0      72\n",
       "        1      47\n",
       "Name: Survived, dtype: int64"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pclass_gender_survival_count_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Agrupando la edad por rango de a 10\n",
    "Age = pd.cut(dftrain['Age'], range(0, 100, 10))\n",
    "dftrain['Age'] = Age\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Cabin</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PassengerId</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>C85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>C123</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>27.0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>14.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>876</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>15.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>880</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>56.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>C50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>881</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>25.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>19.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>B42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>C148</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>342 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             Survived  Pclass  Sex   Age  SibSp  Parch Cabin\n",
       "PassengerId                                                 \n",
       "2                   1       1    0  38.0      1      0   C85\n",
       "3                   1       3    0  26.0      0      0     0\n",
       "4                   1       1    0  35.0      1      0  C123\n",
       "9                   1       3    0  27.0      0      2     0\n",
       "10                  1       2    0  14.0      1      0     0\n",
       "...               ...     ...  ...   ...    ...    ...   ...\n",
       "876                 1       3    0  15.0      0      0     0\n",
       "880                 1       1    0  56.0      0      1   C50\n",
       "881                 1       2    0  25.0      0      1     0\n",
       "888                 1       1    0  19.0      0      0   B42\n",
       "890                 1       1    1  26.0      0      0  C148\n",
       "\n",
       "[342 rows x 7 columns]"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftrain_sobrevivientes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pclass  Age     \n",
       "1       (0, 10]      2.0\n",
       "        (10, 20]    15.0\n",
       "        (20, 30]    29.0\n",
       "        (30, 40]    37.0\n",
       "        (40, 50]    21.0\n",
       "        (50, 60]    15.0\n",
       "        (60, 70]     2.0\n",
       "        (70, 80]     1.0\n",
       "        (80, 90]     NaN\n",
       "2       (0, 10]     17.0\n",
       "        (10, 20]     9.0\n",
       "        (20, 30]    25.0\n",
       "        (30, 40]    19.0\n",
       "        (40, 50]    10.0\n",
       "        (50, 60]     2.0\n",
       "        (60, 70]     1.0\n",
       "        (70, 80]     NaN\n",
       "        (80, 90]     NaN\n",
       "3       (0, 10]     19.0\n",
       "        (10, 20]    20.0\n",
       "        (20, 30]    30.0\n",
       "        (30, 40]    13.0\n",
       "        (40, 50]     2.0\n",
       "        (50, 60]     0.0\n",
       "        (60, 70]     1.0\n",
       "        (70, 80]     0.0\n",
       "        (80, 90]     NaN\n",
       "Name: Survived, dtype: float64"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pclass_gender_survival_count_df= dftrain.groupby(['Pclass','Age'])['Survived'].sum()\n",
    "pclass_gender_survival_count_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
print("prueba1")
