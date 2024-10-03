# FileConstruct

Construct custom files with ease.

## Porting

| Language |    Available   |
|----------|----------------|
| Java     | Yes (Fully)    |
| Python   | Yes            |
| C++      | Planned        |
| Rust     | Planned        |



## Example

Here is a simple example showing how to create a file with the content "Hello, World!" using different types of data.

```Java
import com.github._0x4248.FileConstruct.FileConstructor;


public class HelloWorld {

    public static void main(String[] args) {
        
        // Basic strings
        String HELLO = "Hello";
        String COMMA = ",";
        
        // Single byte
        byte SPACE = (byte) 0x20;
        
        // Byte array
        byte[] WORLD = new byte[] { (byte) 0x57, (byte) 0x6F, (byte) 0x72, (byte) 0x6C, (byte) 0x64 };
        
        // Hex string
        String ENDING = "21 0A";

        // Create a new file constructor
        FileConstructor FC = new FileConstructor();
        FC.filename = "hello_world.txt";
        
        // Add the bytes to the file
        FC.PutASCII(HELLO);
        FC.PutASCII(COMMA);
        FC.PutByte(SPACE);
        FC.PutBytes(WORLD);
        FC.PutHexStr(ENDING);
        
        // Write the file
        FC.Dump();
    }
}
```

### Filling

You can fill a section with a specific byte or a byte array.

```Java

// Fill with a single byte 100 times (200 bytes)
FC.Fill(100, new byte[] { 0x00 });

// Fill with a byte array 100 times (200 bytes)
FC.Fill(100, new byte[] { 0x00, 0x01, 0x02, 0x03, 0x04, 0x05 });

FC.Dump();
```

### Replacing 

```Java
// 01 02 03 04
FC.PutByte((byte) 0x01);
FC.PutByte((byte) 0x02);
FC.PutByte((byte) 0x03);
FC.PutByte((byte) 0x04);

// 01 02 05 04
FC.ReplaceByte(2, (byte) 0x05);
```