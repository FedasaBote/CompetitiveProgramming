func simplifyPath(path string) string {
	stack := []string{}
	curr := ""

	for _, char := range path+string("/") {
		if char == '/' {
			if curr == ".." {
				if len(stack) > 0 {
					stack = pop(stack)
				}
			} else if curr != "." && curr != "" {
				stack = append(stack, curr)
			}
			curr = ""
		} else {
			curr += string(char)
		}
	}

	return "/" + strings.Join(stack, "/")
}

func pop(arr []string) []string {
	arr = arr[:len(arr)-1]
	return arr
}