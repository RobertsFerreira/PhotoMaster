import 'package:flutter/material.dart';
import 'package:photomaster/pages/splash.dart';
import 'package:photomaster/widgets/background/im_bg_without_wave.dart';

class ErrorPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Stack(
      children: <Widget>[
        IMBGW(),
        Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Center(
                child: Text(
                  "Erro ao carregar, verifique sua conexão!",
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 15,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            ),
            IconButton(
              icon: Icon(
                Icons.refresh,
                size: 35,
                color: Colors.white,
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
      ],
    ));
  }
}
