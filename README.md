# Python wrapper for Stanford NER

The unofficial cross-platform Python wrapper for the <b>state-of-art</b> named entity recognition library from Stanford University.

Input: `Google bought IBM for 10 dollars. Mike was happy about this deal.`

Output:
```
Google              	ORGANIZATION
IBM                 	ORGANIZATION
10 dollars          	MONEY
Mike                	PERSON
```

NOTE: It works well on Linux and Ubuntu but it's unclear for Windows.

## About Stanford NER

Named Entity Recognition (NER) labels sequences of words in a text which are the names of things, such as person and company names, or gene and protein names. It comes with well-engineered feature extractors for Named Entity Recognition, and many options for defining feature extractors. Included with the download are good named entity recognizers for English, particularly for the 3 classes (PERSON, ORGANIZATION, LOCATION).

More information can be found here : https://nlp.stanford.edu/software/CRF-NER.shtml

## Installation

First of all, make sure Java 1.8 is installed. Open a terminal and run this command to check:

```bash
java -version
```

If this is not the case and if your OS is Ubuntu, you can install it this way:

```bash
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
```

The code can be invoked either programmatically or through the command line. The program can be invoked with the following commands:

```bash
git clone https://github.com/philipperemy/Stanford-NER-Python.git
cd Stanford-NER-Python
chmod +x init.sh
./init.sh # will run this example above.
```

## Usage

#### Command
```bash
echo "Google bought IBM for 10 dollars. Mike was happy about this deal." > input.txt
python main.py -f input.txt
```

#### Output

```
Google              	ORGANIZATION
IBM                 	ORGANIZATION
10 dollars          	MONEY
Mike                	PERSON
```

## Support

Just open an issue. Any contributions are welcomed!
