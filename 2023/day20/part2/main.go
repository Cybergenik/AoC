package main

import (
	"fmt"
	"os"
	"strings"
    "slices"
    pb "github.com/schollz/progressbar/v3"
)

type FF_Module struct {
	dests []string
	state string
	Module
}

type Con_Module struct {
	dests []string
	state map[string]string
	Module
}

type Pass_Module struct {
	dests []string
	Module
}

type Module interface {
	pulse(input_module string, signal string) string
    destinations() []string
}

type Circuit struct {
	modules map[string]Module
}
func (m *FF_Module) destinations() []string {
	return m.dests
}

func (m *Con_Module) destinations() []string {
	return m.dests
}

func (m *Pass_Module) destinations() []string {
	return m.dests
}

func (m *Pass_Module) pulse(input_module string, signal string) string {
	return signal
}

func (m *FF_Module) pulse(input_module string, signal string) string {
	if signal == "low" {
		if m.state == "on" {
			m.state = "off"
			return "low"
		} else if m.state == "off" {
			m.state = "on"
			return "high"
		}
	}
	return ""
}

func (m *Con_Module) pulse(input_module string, signal string) string {
	m.state[input_module] = signal
	for _, s := range m.state {
		if s == "low" {
			return "high"
		}
	}
	return "low"
}

type QItem struct {
    src string
    sig string
    dst string
}

func (c *Circuit) complete(init_module string, init_signal string) bool {
    q := []QItem{ {src: init_module, sig: init_signal, dst: "broadcaster"} }
    for len(q) > 0 {
        i := q[0]
        q = q[1:]
        if i.sig == "" {
            continue
        }
        //fmt.Printf("%v -%v> %v\n", i.src, i.sig, i.dst)
        if i.dst == "rx" {
            if i.sig == "low" {
                return true
            }
            continue
        }
        out := c.modules[i.dst].pulse(i.src, i.sig)
        for _, d := range c.modules[i.dst].destinations() {
            q = append(q, QItem{src: i.dst, sig: out, dst: d})
        }
    }
    return false
}

func (c *Circuit) add_mod(src string, dests []string) {
	if src[0] == '%' {
		c.modules[src[1:]] = &FF_Module{
			dests: dests,
			state: "off",
		}
	} else if src[0] == '&' {
		c.modules[src[1:]] = &Con_Module{
			dests: dests,
			state: map[string]string{},
		}
	} else {
		c.modules[src] = &Pass_Module{
			dests: dests,
		}
	}

}

func main() {
	file, _ := os.ReadFile("../input.txt")
	c := Circuit{modules: map[string]Module{}}
	for _, l := range strings.Split(string(file), "\n") {
        if l == "" {
            continue
        }
		wf := strings.Split(l, " -> ")
		dests := strings.Split(wf[1], ", ")
		c.add_mod(wf[0], dests)
	}
	for name, mod := range c.modules {
        switch cmod := mod.(type) {
		case *Con_Module:
			for n, mmod := range c.modules {
				if n == name {
					continue
				}
                if slices.Contains(mmod.destinations(), name) {
                    cmod.state[n] = "low"
                }

			}
		}
	}
    N := int64(1000000000)
    bar := pb.Default(N)
    for i := range N {
        if c.complete("button", "low") {
            fmt.Println(i)
        }
        bar.Add(1)
    }
}
