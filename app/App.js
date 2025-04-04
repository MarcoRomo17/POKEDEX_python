import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import login from './login';
import userRegistration from './userRegistration';
import passwordRecover from './passwordRecover';
import editUser from './editUser';


const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="login">
        <Stack.Screen name="login" component={login} />
        <Stack.Screen name="uR" component={userRegistration} />
        <Stack.Screen name="pR" component={passwordRecover} />
        <Stack.Screen name="eU" component={editUser} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
