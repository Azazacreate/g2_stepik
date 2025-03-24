import { Text, View, TextInput, Button, StyleSheet } from "react-native";

const styles = StyleSheet.create({
  container: {
    marginTop: 30,
  },
  top: {
    flexDirection: 'column' ,
  },
  text: {
    fontSize: 30,
    color: 'blue',
  },
  view: {
    backgroundColor: 'pink',
    alignItems: 'center',
  },
  view_1: {
    backgroundColor: 'yellow',
    width: 100,
    height: 100,
  },
  view_2: {
    backgroundColor: 'red',
    width: 100,
    height: 100,
  },
  view_3: {
    backgroundColor: 'gray',
    width: 100,
    height: 100,
  },
});

export default function Index() {
  return (
    <View style={styles.container}>
      <View style={styles.top}>
        <Text style={styles.text}>Hello, my sir Sanal !</Text>
        <Button title="Button" />
      </View>
      <View style={styles.view}>
        <View style={styles.view_1}></View>
        <View style={styles.view_2}></View>
        <View style={styles.view_3}></View>
      </View>
    </View>
  );
}
