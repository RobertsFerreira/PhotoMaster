import 'package:flutter/material.dart';
import 'package:photomaster/pages/splash.dart';

class ErrorPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Center(
              child: Text("Erro ao carregar, verifique sua conexão!"),
            ),
          ),
          IconButton(
            icon: Icon(
              Icons.refresh,
              size: 25,
            ),
            onPressed: () {
              Navigator.pushReplacement(
                context,
                MaterialPageRoute(
                  builder: (context) => Splash(),
                ),
              );
            },
          ),
        ],
      ),
    );
  }
}
