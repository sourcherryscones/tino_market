/*import React from 'react';
import {Text, View} from 'react-native';
import axios from 'axios';
const baseUrl = 'http://192.168.15.224:5001';
const [books, setBooks] = useState([]);


console.log("inside PostList rn")
    axios.get(`${baseUrl}/books`).then((response) => {
      console.log(response.data);
      setBooks(response.data);
      console.log('books set!');
      return response.data;
    })
    .catch(
        function (error) {
          console.log('Show error notification!' + `${baseUrl}/books`)
          return Promise.reject(error)});

const allBookData = () => {
    console.log("made it to allBookData function!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    axios.get(`${baseUrl}/books`).then((response) => {
      console.log(response.data);
      return response.data;
    })
    .catch(
        function (error) {
          console.log('Show error notification!' + `${baseUrl}/books`)
          return Promise.reject(error)});
}

export const PostList = (props: PostProps) => {


    return(
        <div className = "posts">
            {allBookData.map((data,key) => {
                return(
                    <div key={key}>
                        <strong>{data.title}</strong>
                        <p>{data.year}</p>
                    </div>
                );
            })}
        </div>
    );
};
*/