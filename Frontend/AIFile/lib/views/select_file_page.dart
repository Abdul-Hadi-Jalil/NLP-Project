import 'package:flutter/material.dart';
import 'package:file_picker/file_picker.dart';

import '../utils/global/global.dart';

class SelectFilePage extends StatefulWidget {
  const SelectFilePage({super.key});

  @override
  State<SelectFilePage> createState() => _SelectFilePageState();
}

class _SelectFilePageState extends State<SelectFilePage> {
  Future<void> uploadFile() async {
    final result = await FilePicker.platform.pickFiles();
    if (result != null) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('File uploaded successfully!')),
      );
      setState(() {
        Global.file = result.files.first;
        Global.fileName = Global.file!.name;
      });
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('No file selected!')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Select File'),
      ),
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [Color(0xFF2193b0), Colors.lime],
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
          ),
        ),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Global.fileName != null
                  ? Text('Selected File: ${Global.fileName}')
                  : const Text('No file selected'),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: uploadFile,
                child: const Text('Select File'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
