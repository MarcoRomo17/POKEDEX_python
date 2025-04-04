import { useNavigation } from '@react-navigation/native';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image, TextInput, Pressable, Button } from 'react-native';

export default function editUser() {

  const navigation = useNavigation({ navigation })
  return (
    <View style={styles.container}>
        <View style={styles.welcomeTitle}> {/* welcome-title */}
            <Text >Edita tus datos</Text>
        </View>



        <View style={styles.form}>{/* form */}
        <Text style={styles.label}>Cambia los campos que quieras actualizar</Text>{/* label */}

            <Text style={styles.label}>Nombre</Text>{/* label */}
            <TextInput style={styles.input}></TextInput>

            <Text style={styles.label}>Apellidos</Text>{/* label */}
            <TextInput style={styles.input}></TextInput>

            <Text style={styles.label}>Correo</Text>{/* label */}
            <TextInput style={styles.input}></TextInput>

            <Text style={styles.label}>Contraseña</Text>{/* label */}
            <TextInput style={styles.input}></TextInput>

            <Text style={styles.label}>Confirma tu contraseña</Text>{/* label */}
            <TextInput style={styles.input}></TextInput>

            <Pressable 
              onPress={()=> navigation.navigate("login")}
            style={styles.button}><Text style={styles.buttonText}>Cambiar datos</Text></Pressable>



        </View>
     
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: 'aquamarine',
    flex: 1,
    padding:10,
    alignItems: 'center',
    justifyContent: 'center',
 
  },
  title: {
    fontSize: 30,
    fontWeight: 'bold',
    color: 'rgb(83, 89, 254)',
    textAlign: 'center',
    marginTop: 10,  
     width: 400,
    height: 600,
    marginTop: 'auto',
    marginBottom: 'auto',
    justifyContent: 'center',
    flexDirection: 'column',
    alignSelf: 'center',
    padding: 10,
  },
  form: {
    padding: 10,
    flexDirection: 'column',
    justifyContent: 'center',
  },
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
