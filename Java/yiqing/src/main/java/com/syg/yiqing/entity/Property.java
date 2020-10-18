package com.syg.yiqing.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "property")
public class Property {
    @Id // 该字段对应数据库中的列为主键
    @GeneratedValue(strategy = GenerationType.IDENTITY) // 主键自增长
    @Column(name = "id") // 对应tradition_office表中的id列
    private Integer id;

    @Column(name = "name")
    private String name;

    @Column(name = "href")
    private String href;

    @Column(name = "president_info")
    private String president_info;
}
