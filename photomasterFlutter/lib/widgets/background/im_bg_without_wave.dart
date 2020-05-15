import 'package:flutter/material.dart';

class IMBGW extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.fromLTRB(10, 20, 10, 20),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          begin: Alignment.topCenter,
          end: Alignment.bottomCenter,
          stops: [0.1, 1.2],
          colors: [
            Color(0xFFF92B7F),
            Color(0xFFF58524),
          ],
        ),
      ),
    );
  }
}
