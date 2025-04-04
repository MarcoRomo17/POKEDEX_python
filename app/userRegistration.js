import { useNavigation } from '@react-navigation/native';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image, TextInput, Pressable, Button } from 'react-native';

export default function userRegistration() {

  const navigation = useNavigation()

  return (
    <View style={styles.container}>
        <View style={styles.welcomeTitle}> {/* welcome-title */}
            <Text>Registrate aquí</Text>
        </View>

        <View style={styles.imgContainer}>{/* img-container */}
            <Image  style={styles.imgContainer.img}source={{uri:"https://pbs.twimg.com/profile_images/1776012369409294338/HIwZDIlC_400x400.jpg"}}></Image>
        </View>

        <View style={styles.form}>{/* form */}
            <Text style={styles.form.label}>Ingresa tu nombre</Text>{/* label */}
            <TextInput style={styles.form.input}></TextInput>

            <Text style={styles.form.label}>Ingresa tus apellidos</Text>{/* label */}
            <TextInput style={styles.form.input}></TextInput>

            <Text style={styles.form.label}>Ingresa tu Correo</Text>{/* label */}
            <TextInput style={styles.form.input}></TextInput>

            <Text style={styles.form.label}>Ingresa tu contraseña</Text>{/* label */}
            <TextInput style={styles.form.input}></TextInput>

            <Text style={styles.form.label}>Confirma tu contraseña</Text>{/* label */}
            <TextInput style={styles.form.input}></TextInput>

            <Pressable style={styles.button}
              onPress={()=> navigation.navigate("login")}
            
            ><Text style={styles.buttonText}>Registrarme</Text></Pressable>



        </View>
     
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: 'aquamarine',
    flex: 1,
    width: 400,
    justifyContent: 'center',
    alignSelf: 'center',
    padding: 10,
  },
  welcomeTitle: {
    fontSize: 30,
    fontWeight: 'bold',
    color: 'rgb(254, 248, 83)',
    textAlign: 'center',
    marginBottom: 20,
  },
  imgContainer: {
    alignItems: 'center',
    marginBottom: 20,
    img: {
      width: 200,
      height: 200,
      borderRadius: 100, // 60% border radius visual en RN
    },
  },
  form: {
    padding: 10,
    justifyContent: 'center',
    input: {
      borderRadius:10,
      borderWidth:2,
      borderColor:"black",
      fontSize:15,
      width:"auto",
      fontSize:20,
      backgroundColor:"#fff"
    },
    label: {
      marginBottom: 5,
      fontWeight: 'bold',
      marginLeft: 10,
    },
  },
  button: {
    marginTop: 15,
    alignSelf: 'center',
    borderRadius: 10,
    backgroundColor: 'rgb(83, 89, 254)',
    paddingVertical: 10,
    paddingHorizontal: 20,
  },
  buttonText: {
    color: '#fff',
    fontWeight: 'bold',
  },
});