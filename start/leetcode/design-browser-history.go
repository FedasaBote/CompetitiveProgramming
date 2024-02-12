import (
	"container/list"
	"fmt"
)

type BrowserHistory struct {
	forward     *list.List
	backward    *list.List
	currentUrl  string
}

func Constructor(homepage string) BrowserHistory {
	return BrowserHistory{
		forward:     list.New(),
		backward:    list.New(),
		currentUrl:  homepage,
	}
}

func (this *BrowserHistory) Visit(url string) {
	this.backward.PushBack(this.currentUrl)
	this.forward = list.New()
	this.currentUrl = url
}

func (this *BrowserHistory) Back(steps int) string {
	for steps > 0 && this.backward.Len() > 0 {
		this.forward.PushBack(this.currentUrl)
		this.currentUrl = this.backward.Remove(this.backward.Back()).(string)
		steps--
	}
	return this.currentUrl
}

func (this *BrowserHistory) Forward(steps int) string {
	for steps > 0 && this.forward.Len() > 0 {
		this.backward.PushBack(this.currentUrl)
		this.currentUrl = this.forward.Remove(this.forward.Back()).(string)
		steps--
	}
	return this.currentUrl
}