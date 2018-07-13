# File structure:
* *something*Listing.txt : a list of category triplets for the corresponding type of product
* *something*Reviews.txt : set of reviews for inter annotator agreement in raw form
* *something*Reviews.xml : set of reviews for inter annotator agreement in xml format
* *something*Reviews2.txt : set of reviews for second part in raw form
* *something*Reviews2.xml : set of reviews for second part in xml format

## XML format
The xm files follow the convention set by the organisers of [SemEval 2016, Task 5](http://www.aclweb.org/anthology/S16-1002), which is described below:

```
<Reviews>
    <Review id="some number">
        <sentences>
            <sentence>
                <text>This is my sentence</text>
                <Opinions>
                    <Opinion category="A#B#C" polarity="positive/negative/neutral" implicit="true/false/coreference" />
                </Opinions>
            </sentence>
        </sentences>
    </Review>
</Reviews>
```

> Made during the summer of 2018 at HLTRI@UT Dallas.