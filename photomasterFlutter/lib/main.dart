import 'package:flutter/material.dart';
import 'package:photomaster/pages/splash.dart';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Photo Master',
      theme: ThemeData(
        fontFamily: 'Caviar',
      ),
      debugShowCheckedModeBanner: false,
      home: Splash(),
    );
  }
}
