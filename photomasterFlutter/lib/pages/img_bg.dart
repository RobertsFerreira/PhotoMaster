import 'package:flutter/material.dart';
import 'package:wave/config.dart';
import 'package:wave/wave.dart';

class IMGBG extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        height: 1000, //atura que a wave irá tomar
        child: RotatedBox(
          quarterTurns: 2, //numero de waves desejado
          child: WaveWidget(
            config: CustomConfig(
              gradients: [
                [Color(0xFFF92B7F), Color(0xFFF58524)],
                [Color(0xFFF92B7F), Color(0xFFF58524)],
              ],
              durations: [20000, 16000], //velocidade da wave
              heightPercentages: [0.15, 0.20], //tamanho da wave
              blur: MaskFilter.blur(BlurStyle.solid, 10), //blur da wave deixa
              gradientBegin: Alignment.bottomCenter,
              gradientEnd: Alignment.topCenter,
            ),
            waveAmplitude: 0,
            size: Size(double.infinity, double.infinity), //Size lateral da wave
          ),
        ),
      ),
    );
  }
}
