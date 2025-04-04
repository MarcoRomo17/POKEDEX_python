import { useNavigation } from '@react-navigation/native';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image, TextInput, Pressable } from 'react-native';

export default function login() {
  const navigation= useNavigation()
  return (
    <View style={styles.container}>
      <View> 
          <Image source={{uri:"https//upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/2052px-Pok%C3%A9_Ball_icon.svg.png"}}
          width={200}
          height={200}></Image>

        </View>

      <View>
          <Text style={styles.title}>Iniciar sesion</Text>{/* title */}
          <Text style={styles.label}>Correo:</Text> {/* label */}
          <TextInput style={styles.input}></TextInput>
          <Text style={styles.label}>Contraseña</Text>{/* label */}
          <TextInput style={styles.input}></TextInput>

          <Pressable style={styles.send} title='Enviar'
          onPress={() => navigation.navigate('eU')}
          ><Text style={styles.send.textButton}>Enviar</Text></Pressable>

      </View>

      <View style={styles.containerFooter}>{/* container footer */}
          <Text
          onPress={()=> navigation.navigate("pR")}
          style={styles.containerFooter.texts}>Olvidaste tu contraseña</Text>
          <Text
          onPress={()=> navigation.navigate("uR")}
          style={styles.containerFooter.texts}>Registrate</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    padding:10,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title:{
    fontSize:30,
    fontWeight:"bold"
  },
  label:{
    fontSize:20,
    fontWeight:"bold"
  },
  input:{
    borderRadius:10,
    borderWidth:2,
    borderColor:"black",
    fontSize:15,
    width:"auto",
    fontSize:20
  },
  send:{
    backgroundColor:"red",
    width:"auto",
    height:"auto",
    borderRadius:10,
    marginTop:15,
    alignItems:"center",
    
    textButton:{
      color:"white",
      fontWeight:"bold",
      fontSize:20
    }
  },
  containerFooter:{
    justifyContent:"center",
    alignItems:"center",
    texts:{
      fontSize:20,
      margin:5
      
    }
  }



});
