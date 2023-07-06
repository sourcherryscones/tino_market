import { StatusBar } from 'expo-status-bar';
import {useState} from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
//import {PostList} from './PostList.js'

import axios from 'axios';
const baseUrl = 'http://192.168.15.224:5001';
const [books, setBooks] = useState([])

function allBookData(){
    console.log("made it to allBookData function!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    axios.get(`${baseUrl}/books`).then((response) => {
      console.log(response.data);
      setBooks(response.data);
      return response.data;
    })
    .catch(
        function (error) {
          console.log('Show error notification!' + `${baseUrl}/books`)
          return Promise.reject(error)});
}


export default function App() {
  return (
    <View style={styles.container}>
      <Text>Close down App.js to start working on your app!</Text>
      <LotsOfGreetings/>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
